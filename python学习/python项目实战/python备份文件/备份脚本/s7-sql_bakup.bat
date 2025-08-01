@echo off
set MYSQL_BIN="D:\Mysql\mysql_x64\bin\mysqldump.exe"
set BACKUP_DIR="E:\data_bak\s7_sql_bak"
set WINRAR="C:\Program Files (x86)\WinRAR\WinRAR.exe"

:: ���Ŀ¼�Ƿ���ڣ���Ȩ��ʱ����ʾ
if not exist %BACKUP_DIR% (
    mkdir %BACKUP_DIR%
    if errorlevel 1 (
        echo [����] �޷�����Ŀ¼ %BACKUP_DIR%������Ȩ�޻�·����
        pause
        exit /b
    )
)

:: ��� WinRAR �Ƿ����
if not exist %WINRAR% (
    echo [����] WinRAR δ�ҵ������޸�·����%WINRAR%
    pause
    exit /b
)

:: ��ȡ���ں�ʱ��
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value 2^>nul') do set "datetime=%%a"
if "%datetime%"=="" (
    echo [����] �޷���ȡϵͳʱ�䣬���� wmic ���
    pause
    exit /b
)
set "current_date=%datetime:~0,4%%datetime:~4,2%%datetime:~6,2%"
set "current_time=%datetime:~8,2%%datetime:~10,2%"

:: �����ļ���
set BACKUP_FILE=%BACKUP_DIR%\s7_backup_%current_date%_%current_time%.sql
set ZIP_FILE=%BACKUP_DIR%\s7_backup_%current_date%_%current_time%.zip

:: ִ�� MySQL ���ݣ�����ʱ����ͣ��
echo ���ڱ������ݿ�...
%MYSQL_BIN% -h 127.0.0.1 -P 3308 -u root -p123456 s7 > %BACKUP_FILE%
if errorlevel 1 (
    echo [����] MySQL ����ʧ�ܣ��������Ӳ��������ݿ�״̬��
    pause
    exit /b
)

:: ѹ��Ϊ ZIP
echo ����ѹ�������ļ�...
%WINRAR% a -afzip -r -df -ep1 -ibck %ZIP_FILE% %BACKUP_FILE%
if errorlevel 1 (
    echo [����] ѹ��ʧ�ܣ����� WinRAR ���ļ�Ȩ�ޣ�
    pause
    exit /b
)

:: ��¼��־
echo [%date% %time%] ���ݳɹ�: %ZIP_FILE% >> %BACKUP_DIR%\backup_log.txt

:: ����90��ǰ�ı��ݣ���Ĭִ�У�������ʾ��
forfiles /p %BACKUP_DIR% /m *.zip /d -90 /c "cmd /c del @path" 2>nul

echo ������ɣ�%ZIP_FILE%