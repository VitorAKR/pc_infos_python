#!/usr/bin/env python
# coding: utf-8

# In[27]:


#importar a biblioteca WMI - Windows Management Instrumentation
import wmi


# In[28]:


#instanciar pc e os
pc = wmi.WMI()
mySystem = pc.Win32_ComputerSystem()[0]
os = pc.Win32_OperatingSystem()[0]


# In[50]:


#apresentar Infos
print(f"Nome: {mySystem.Name}")
print(f"Modelo: {mySystem.Model}")
print(f"Marca: {mySystem.Manufacturer}")
print(f"Família: {mySystem.SystemFamily}")
print(f"Quantidade de CPUs: {mySystem.NumberOfProcessors}")
print(f"Arquitetura: {mySystem.SystemType}")
print(f"Usuário: {mySystem.UserName}")
print(f"Boot: {mySystem.BootupState}")
print(f"Boot Device: {os.BootDevice}")
print(f"Sistema Operacional: {os.Name}")
print(f"Número da Build: {os.BuildNumber}")
print(f"Número de Série: {os.SerialNumber}")
print(f"Versão: {os.Version}")

