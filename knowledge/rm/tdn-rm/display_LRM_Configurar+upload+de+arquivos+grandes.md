---
content_hash: 138ea733bee50515a868a5e111ae47a22e34292dc6db6da87391234de10c9d1b
fetched_at: '2026-06-29T00:12:02.261188+00:00'
page_id: '899214321'
product: rm
source: tdn-rm
title: Configurar upload de arquivos grandes
type: documentation
url: https://tdn.totvs.com/display/LRM/Configurar+upload+de+arquivos+grandes
version: 32
---

O objetivo desta documentação é auxiliar as instituições na configuração para **aumentar o tamanho máximo de upload** da ferramenta **IIS(Internet Information Services)** dos portais **Portal Educacional / Portal do Professor / Portal Gestão Educacional** .

Caso o cliente deseja que seja realizado uploads com tamanho superior ao tamanho padrão (**30mb**) **IIS(Internet Information Services)** será necessário realizar os seguintes passos.

O **tamanho padrão máximo de upload**do **IIS(Internet Information Services)** é de **30mb**

O **tamanho máximo para upload** depende da configuração do ambiente de cada cliente, que é responsável por definir o tamanho desejado.

Lembrando que este o tamanho máximo permitido, deve ser compatível com o **maior tamanho parametrizado do RM.exe para os portais.**

O **tamanho do arquivo** ao ser carregado pelo portal, tem variação em seu tamanho real, o que gera um **acréscimo 33%** em relação ao tamanho informado na parametrização do **RM.exe**.

**Exemplo:**

**Maior parametrização do RM.exe:** **50mb**

**33 % da maior parametrização do RM.exe: 16,50mb**

**Tamanho a ser configurado no IIS: 50mb + 16,50mb = 66,50mb (convertido em bytes 66500000)**

Conforme citado, a configuração de **tamanho máximo de upalod** de uma requisição é uma medida de segurança para o servidor Web.

Sendo assim, **não é recomendado que se permita** requisições com tamanho muito grande. Em casos de ataques, como por exemplo uma negação de serviço, o envio de requisições de grande volume pode facilitar a ação de pessoas mal-intencionadas, tornando o servidor mais vulnerável.

Todas as informações apresentadas foram verificadas e testadas em um ambiente controlado. Contudo, devido à diversidade e complexidade das configurações, bem como às particularidades dos servidores de cada cliente, recomenda-se que as alterações sejam inicialmente realizadas em um ambiente de homologação.

Em alguns casos é necessário configurar o tempo de time out dos portais também. Saiba mais em [Configurar tempo de timeout do portal](https://tdn.totvs.com/display/LRM/Configurar+tempo+de+timeout+do+portal)

**Os tamanhos máximos de upload** exibidos nas imagens abaixo são **m**e**ramente ilustrativos**.

## **CONFIGURAÇÕES**

**1)** Acesse o **IIS(Internet Information Services).**

**2)** Selecione a pasta desejada:

Definição de uma das opções abaixo

Existe **duas possibilidades** que a instituição pode adotar para aumentar **o tamanho máximo de upload.**

A **própria instituição deve avaliar e definir a opção** que melhor se adapta ao seu cenário

Opção 1: Configuração padrão para todo os portais do FrameHTML

A configuração do **tamanho padrão máximo de upload** para todos os sites que estão dentro do diretório do **FrameHTML**. Lembrando que esta opção inclui outro produtos da TOTVS, além do Educacional, caso o cliente possua.

* **Todos os portais, selecione a pasta: "**Sites\Default Web Site\FrameHTML****"****
Opção 2: Configuração por cada portal individual

A configuração do **tamanho máximo de upload** individual para cada portal educacional que estão dentro do diretório do **FrameHTML**. 

Portal do aluno

Para configurar o portal do aluno, é necessário seguir os passos abaixo:

**1)** Acesse o diretório que os portais **"FrameHTML"** e selecione a pasta **"RM".**

**2)** Criar uma pasta **"API"** e acessa-la. 

**3)** Criar a pasta "**TOTVSEducacional**" e acessa-la. 

**4)** Criar um arquivo "**web.config**" conforme o padrão abaixo:

 

Sugestão de configuração

]]>

**5) S****elecione a pasta: **Sites\Default Web Site\FrameHTML\RM\API\TOTVSEducacional****

Portal do professor

**S****elecione a pasta: **Sites\Default Web Site\FrameHTML\web\app\Edu\portaldoprofessor****

Portal do gestão educacional

**S****elecione a pasta: **Sites\Default Web Site\FrameHTML\web\app\Edu\portalgestaoeducacional****

**As imagens abaixo são apenas um exemplo** utilizando a pasta padrão FrameHTML, **mas deverá selecionar a pasta conforme definido acima pela instituição**.

**3)** Clique na opção "**Filtragem de Solicitações**".

**4)** Selecione a opção do menu "Editar Configurações de Recurso"

**5)** Um nova janela será aberta, dentro do agrupamento "**Limites da Solicitação**" defina o campo "**Tamanho máximo de conteúdo permitido (Bytes)**" com o tamanho máximo que deseja receber requisições.

O tamanho preenchido dependerá da configuração do ambiente de cada cliente. Sendo ele responsável por esta definição.

Lembrando que este o tamanho máximo permitido, deve ser compatível com o **maior tamanho parametrizado do RM.exe para o portal do aluno.**

O tamanho do campo é definido em **Bytes**

**6)** Clique na opção "**Editor de configurações**".

**7)** Selecione a seção"**system.web/httpRuntime**".

**8)** Dentro da lista de opções defina o campo "**maxRequestLength**" com o tamanho máximo que deseja receber requisições.

O tamanho preenchido dependerá da configuração do ambiente de cada cliente. Sendo ele responsável por esta definição.

Lembrando que este o tamanho máximo permitido deve ser compatível com o **maior tamanho parametrizado do RM.exe para o portal.**

O tamanho do campo é definido em **Bytes**

**9)** Clique no botão "Aplicar"

**10)** Ao final do processo reinicia o IIS para efetivar todas as alterações
