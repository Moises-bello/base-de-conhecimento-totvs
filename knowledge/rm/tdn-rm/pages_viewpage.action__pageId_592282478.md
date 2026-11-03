---
content_hash: 6127d6739dc5817dfcc33680cccfe20c870555527b909c400863ecef6ec85b08
fetched_at: '2026-06-29T00:10:56.235078+00:00'
page_id: '592282478'
product: rm
source: tdn-rm
title: Portal de Imóveis - Backend - Globais - Situação Cadastro Pessoa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=592282478
version: 16
---

Situação cadastro Pessoa

Trata-se de uma opção que permite mapear opções de Avanços de situações, que serão utilizadas ao realizar avanços de uma pessoa.

**1)** Para realizar este mapeamento de situação de pessoas, acesse: Globais > Situação Cadastro Pessoas;

**2)** Em seguida *(ao clicar em Adicionar)* realize os cadastros referentes aos avanços;  
  
  
  
**3)** Ao realizar a edição destes registros, será necessário vincular este a um próximo avanço que será realizado *(quando esta opção estiver sendo utilizada no avanço de Leads)*. Pode-se associar uma situação à outras N situações para as quais este cadastro pode estar, não necessariamente a apenas uma.

***OBS:*** ***A partir deste momento ao acessar o cadastro de Pessoas é possível visualizar respectivamente cada uma destas situações destacadas na visão de acordo com a parametrização cadastrada. Lembrando que estes avanços são realizados a partir do [Funil de leads](https://tdn.totvs.com/pages/viewpage.action?pageId=699798402).***  
  
**Configurar a Situação Pessoa do Lead que possui Funil Integrado do RD Station.**

---

Para que a situação de uma pessoa **(que possui funil parametrizado)** seja apresentada no Portal de imóveis **(quando este for marcado como uma oportunidade)** será necessário realizar algumas parametrizações. *Importante destacar que a entidade que vincula estes registros será o Empreendimento*.  
  
Veja na prática a inclusão de um campo de empreendimento no RD Station:  
  
**1)** No cadastro de Leads do RD Station insira um campo personalizado de empreendimento ;

**2)** Realize as parametrizações informando os nomes dos Empreendimentos existentes na base de dados do Portal de Imóveis:

**3)** Informe no cadastro deste Lead qual é o empreendimento que o mesmo possui parametrizado (salve estas informações):

**4)** Em seguida , no portal de Imóveis, acesse > Backend > Campos personalizados, será necessário integrar o campo de Empreendimento criado no RD Station com o Portal de imóveis  
Mais informações sobre toda esta funcionalidade encontra-se descrito no link: ***[Configuração de campos no RD Station integrados com o Portal de Imóveis:](https://tdn.totvs.com/pages/releaseview.action?pageId=687737814#RDSTATION-854665619)***

**5)** Acesse o cadastro de Funil, e realize a edição do Funil que terá a Situação de entrada parametrizada. Em seguida selecione no campo (Situação de entrada de Lead) que será a situação apresentada quando o lead for marcado como oportunidade, seguida clique em Salvar.

Mais informações sobre: Sincronizando Funil do Lead com RD Staton, acesse: ***[Sincronizando Funil do RD Station com o Portal de Imóveis](https://tdn.totvs.com/pages/releaseview.action?pageId=699798333)***

### Funcionalidade: Parâmetro de Etapa "Sem Contato (Sem Atendimento)" no Funil de Leads Integrado ao RD Station

Foi criada uma funcionalidade que permite definir uma etapa específica no funil de leads, integrado ao RD Station, como **"Sem Contato (Sem Atendimento)"**. Essa etapa indica que o corretor ainda **não iniciou o atendimento ao lead**.

Essa definição é essencial para que a **roleta de vendas do PI** saiba se deve redistribuir o lead para outro corretor após o tempo limite configurado.

#### Regras de funcionamento:

* **Apenas uma etapa por funil de leads** pode ser marcada como "Sem Contato (Sem Atendimento)".
* Caso **nenhuma etapa** esteja marcada como tal em um funil do RD Station, a **roleta de vendas seguirá a lógica padrão** do PI para identificar se o lead está em atendimento ou não.

#### Objetivo da funcionalidade:

Quando a roleta de vendas do PI distribui um lead para um corretor:

* O corretor será **atualizado automaticamente** tanto na negociação do **RD CRM** quanto como **dono do lead no RD Marketing**.
* A roleta funcionará da seguinte forma:

  1. **Se o lead foi atendido** (ou seja, a negociação **não** está na etapa definida como "Sem Contato"):

     + O lead **não será redistribuído** após o tempo limite da roleta.
  2. **Se o lead não foi atendido** (ou seja, a negociação permanece na etapa definida como "Sem Contato"):

     + O lead **será redistribuído para outro corretor** após o tempo limite.
     + O novo corretor será atualizado na negociação do **RD CRM**, no dono do lead no **RD MKT**, e também no **Cadastro de Pessoas**.

**6)** Ao acessar o cadastro de Situação Pessoas Será possível visualizar a situação que foi importada para o Portal de Imóveis.

***OBS: No Funil do Lead o registro já será apresentado com a situação do Lead atualizado.***  
***Mais informações referentes a funil do Lead acesse: [Pré- Venda - Funil de Leads](https://tdn.totvs.com/pages/releaseview.action?pageId=699798402)***

***Caso tenha o mesmo empreendimento em mais de um funil, o sistema irá buscar a situação do primeiro encontrado.***
