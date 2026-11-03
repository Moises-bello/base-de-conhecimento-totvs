---
article_id: 360034038393
category: TAF - eSocial - Instalação
content_hash: 6dd425b57d3ea12d80edecec69915f182f3614ef936706e50b74f4e0f3ec373f
fetched_at: '2026-06-28T22:45:11.010694+00:00'
product: protheus
section_id: 1500001536881
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Instalação- INSTALADOR - Pré-requisitos
type: support-article
updated_at: '2026-01-08T17:46:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034038393-RH-Linha-Protheus-TAF-eSocial-Instala%C3%A7%C3%A3o-INSTALADOR-Pr%C3%A9-requisitos
---

**Dúvida**

**ATENÇÃO:** *Clientes que de alguma forma perderam a instalação do TAF porém tem seus dados armazenados no banco de dados em backup é recomendável que este processo seja executado por um consultor in loco **qualificado**para executar a instalação.*

Como verificar e analisar os pré-requisitos que o sistema exige para o correto funcionamento do TAF?

**Sistema Operacional:**  
O instalador foi projetado para rodar apenas em ambiente Windows;

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Instalação - Instalador – À partir da versão 12.1.27

**Solução**

1 - Verifique os requisitos mínimos em seu servidor baixando o arquivo abaixo:

[Infraestrutura mínima](http://tdn.totvs.com/download/attachments/190517377/Infraestrutura%20minina%20TAF.pdf?version=1&modificationDate=1521576323000&api=v2)

**Obs.:** À partir desta instalação, a arquitetura foi desenvolvida para uso somente em sistemas operacionais 64 bits homologados, permitindo a simplificação e melhor utilização de infraestrutura.

2 - Verifique a versão do .NET Framework. A versão do >NET Framework deverá ser igual ou superior a 4.6.1. Caso tenha dúvidas, acesse a documentação abaixo:  
[RH - Linha Protheus - TAF - eSocial - Microsoft.Win32.RegistryKey.CreateSubKey(System.String, Boolean)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046004853)

3 - Banco de Dados (SQL ou ORACLE) criado e vazio ([Bancos Homologados para o TAF](https://tdn.totvs.com/x/P4pc));   
**(Caso queira instalar com um banco diferente de SQL ou ORACLE, necessário realizar a instalação do TAF de maneira manual)**;

4 - É necessário que a autenticação de acesso ao banco de dados seja através de uma senha do SGBD ou uma autenticação mista, ou seja, através de uma senha do SGBD. A autenticação automática pelo Sistema Operacional não inicializa o serviço.

5 -**Banco de dados:**Antes de qualquer processo da instalação do TAF e do TSS, devem ser criadas duas bases no banco de dados. Dêem preferência com o nome igual ao do sistema que estão instalando:

**Exemplo:**

Veja o exemplo abaixo no SQL Express:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043937073)

**Obs.:**Importante verificar e parametrizar o Collation correto.

[Veja aqui os parâmetros do Collation](https://tdn.totvs.com/display/tec/DBAccess+-+Collation%2C+Character+Type+e+Encoding)

6 - **Conexão ODBC:** Com o instalador do TAF e do TSS, a conexão ODBC será criado automaticamente pelo sistema. Caso queira consultar como é feito a criação temos uma documentação que auxilia na conexão ODBC:

[RH - Linha Protheus - TAF - eSocial - Cofiguração - Como criar uma fonte de dados (ODBC 64 bits) para uso com Microsoft SQL Server](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034281974)

7 - **Conexão Oracle:**Para conexões Oracle, possuímos outra documentação abaixo:

[RH - Linha Protheus - TAF - eSocial - CONFIGURAÇÃO - Criando conexão com banco Oracle](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035186814)

8 - **License Server:** É necessário que o servidor de licenças esteja atualizado com a versão igual ou acima da 3.2.0 para realizar a instalação do TAF:  
<https://tdn.totvs.com/display/framework/TOTVS+License+Server+Virtual>

9 - Para realizar o download do TAF e do TSS, acesse o link:

[RH - Linha Protheus - TAF - eSocial - Como baixar o instalador do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033541434)
