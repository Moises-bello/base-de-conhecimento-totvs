---
content_hash: b86c7e0d8a7498e54c3ed05104f663646ee2c182b54ae6fd8e0f6a7cc80a6f1d
fetched_at: '2026-06-29T00:05:57.772108+00:00'
page_id: '181966739'
product: rm
source: tdn-rm
title: RM Portal carrega a tela de login em branco
type: documentation
url: https://tdn.totvs.com/display/LRM/RM+Portal+carrega+a+tela+de+login+em+branco
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework                         **Versão:** 11.xx |
| **Processo** | **:** | RM Portal |
| **Subprocesso** | **:** | RM Portal carrega a tela de login em branco |
| **Data da publicação** | **:** | 16/01/2015 |

Verifique se o ambiente no qual está sendo instalado o RM Portal se encontra de acordo com a Portabilidade da versão instalada:

Portabilidade da Linha RM Versão 11.52

<http://tdn.totvs.com/pages/releaseview.action?pageId=59900404>

[Portabilidade da Linha RM Versão 11.82](http://tdn.totvs.com/pages/releaseview.action?pageId=59900404)

<http://tdn.totvs.com/pages/releaseview.action?pageId=60522502>

[Portabilidade da Linha RM Versão 12.01](http://tdn.totvs.com/pages/releaseview.action?pageId=60522502)

<http://tdn.totvs.com/pages/releaseview.action?pageId=165282824>

Para perfeito funcionamento do RM Portal, faz-se necessário que o IIS esteja instalado e funcionando corretamente.

Para confirmar se o IIS está funcional, digite "localhost" no Browser no Servidor de Portal e confirme se a página do IIS será carregada:

Verifique como está a Parametrização Global – URL de acesso ao portal. Através do link abaixo:

<http://tdn.totvs.com/pages/releaseview.action?pageId=61932793>

Após realizar a parametrização realize o teste no RM Portal.

Caso o teste não seja positivo realize o processo abaixo.

Inicialmente terá que verificar pelo menos dois processos:

a)Refazer o arquivo \_Broker.dat, pois este arquivo contém informações para a constituição da página web.

1. Verificar no arquivo RM.Host.Service.exe.config (C:\totvs\CorporeRM\RM.Net) se a tag ActionsPath, está com o endereço físico da pasta rm.net correto. Exemplo:

Efetuei a instalação no endereço c:\totvs\. A tag neste caso ficaria:

<add key="ActionsPath" value="C:\totvs\CorporeRM\RM.Net;C:\totvs\CorporeRM\Corpore.Net\Bin" />

Conforme print abaixo:

Após o procedimento acima, execute o procedimento abaixo:

1. Acessar o Explorer da máquina e ir à pasta "C:\totvs\CorporeRM\RM.Net".
2. Dentro da pasta RM.Net encontrar o arquivo "RM.Host.ServiceManager.exe".
3. Clicar duas vezes sobre o mesmo.
4. O formulário a seguir deverá ter o botão "desinstalar" habilitado e o label (texto em negrito) com seu status igual a "Iniciado".
5. Clique no botão "desinstalar" até o label (texto em negrito) ficar com seu status de "Serviço não existe".
6. Volte para a pasta RM.Net e encontre dentro da mesma o arquivo chamado \_Broker.dat".
7. Selecione o arquivo e apague o mesmo.
8. Volte para o arquivo "RM.Host.ServiceManager.exe" ou clique novamente no mesmo (caso tenha fechado o mesmo anteriormente).
9. Agora deverá ter habilitado o botão "instalar".
10. Clique no botão "instalar" até o label (texto em negrito) atingir o status "Iniciado".

b)Verificação de 2 ou 3 camadas:

Se estiver em 3 camadas, provavelmente a instalação do portal está configurada em 2 camadas.

Como conferir:

1. Acesse/ abra o arquivo RM.Host.Service.exe.config (C:\totvs\CorporeRM\RM.Net).
2. Confira a tag key="JobServer3Camadas".
3. Acesse / abra em bloco de notas o arquivo Web.config (C:\totvs\CorporeRM\Corpore.Net).
4. Localize também a  tag "JobServer3Camadas".

O valor nesta tag tem que estar true

Na mesma linha de raciocínio, ou melhor, nos mesmos arquivos / endereço, verificar a tag: <add key="EnableCompression" value="true" />

Em ambos os arquivos, o valor tem que ser idêntico. Recomendamos o true.

**Observação:** Considerando 3camadas a tag    <add key="Host" value="localhost" />, o valor deve apontar para o servidor de aplicação. Qualquer alteração de valor, é obrigatório que reinicie o serviço de Host.

Caso a instalação seja local, o valor das tags deve ser false:

Após todos os processos, reinicie o IIS:

Iniciar > executar > digite  IISRESET

**Outra dica:**

Registrar novamente o IIS sendo:  
  
**Para ativação do IIS:**

1 - Acesse a pasta:

Caso seja Windows 64Bits: C:\Windows\Microsoft.NET\Framework64\v4.0.30319

Caso seja Windows 32Bits: C:\Windows\Microsoft.NET\Framework\v4.0.30319

2 - Localize e execute o arquivo: **aspnet\_regiis.exe**

3 - Copie o caminho onde o arquivo está localizado:

Windows 64Bits C:\Windows\Microsoft.NET\Framework64\v4.0.30319

Windows 32Bits C:\Windows\Microsoft.NET\Framework\v4.0.30319

4 – Abra o promt de comando com usuário administrador

5 – Digite CD, pressione a tecla “Espaço” cole o caminho e pressione a tecla “Enter”

6 – Execute o comando:

Windows Server 2008, 2008R2 e 2012

**aspnet\_regiis.exe -i**

Windows Server 2012R2 e superiores:

**dism /online /enable-feature /featurename:IIS-ASPNET45 /all** 

**Reinicie o IIS:**

Executar: CMD (Prompt de Comando DOS)

Digite o comando: IISRESET

Após registrar novamente o IIS, teste o portal.   
  
**Testes:**

**Efetue testes sempre de forma local, ou seja, direto do seu Servidor de Web.**

Através do navegador IE ou Firefox, digite <http://localhost/corpore.net/Login.aspx>

Com isso, verifique se o empecilho foi resolvido.

Caso contrário, sugerimos a reinstalação do RM Portal, seguindo as orientações do Manual "Instalação do Portal WEB":

<http://tdn.totvs.com/pages/viewpage.action?pageId=59900164>

Para maiores informações:

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha);
