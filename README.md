# pc_infos_python
Script em Python que pega informações da máquina e sistema operacional usando a biblioteca WMI.

### Instale a biblioteca

Use o package manager [pip](https://pypi.org/project/WMI/) para instalar a biblioteca WMI - Windows Management Instrumentation.
Abra um console e digite o comando abaixo, faça isso antes de rodar o script.

```bash
pip install wmi
```

### Como rodar o script?

Para utilizar o script rode o seguinte comando na console:

```bash
python pc_python_script.py
```

O Resultado será algo parecido com isto no retorno:
```bash
Nome: LAPTOP-*******
Modelo: Aspire ****-***
Marca: Acer
Família: Aspire 5
Quantidade de CPUs: 1
Arquitetura: x64-based PC
Usuário: LAPTOP-********\***Seu Usuario***
Boot: Normal boot
Boot Device: \Device\HarddiskVolume1
Sistema Operacional: Microsoft Windows 10 Home Single Language|C:\WINDOWS|\Device\Harddisk0\Partition3
Número da Build: ******
Número de Série: *****-*****-*****-*****
Versão: 10.0.*****
```
