---
article_id: 360020656692
category: NFe - Nota Fiscal Eletrônica
content_hash: 256a793baeae7a1c97d01cb3b8db6b247e37d07a028b8c32b35660d7b8f02a7c
fetched_at: '2026-06-28T22:40:05.074753+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 510 Rejeição :
  Operação com Exterior e Código País destinatário é 1058 (Brasil) ou não informado'
type: support-article
updated_at: '2025-07-14T14:10:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020656692-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-510-Rejei%C3%A7%C3%A3o-Opera%C3%A7%C3%A3o-com-Exterior-e-C%C3%B3digo-Pa%C3%ADs-destinat%C3%A1rio-%C3%A9-1058-Brasil-ou-n%C3%A3o-informado
---

**Dúvida**Como corrigir arejeição 510 : Operação com Exterior e Código País destinatário é 1058 (Brasil) ou não informado

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

1. Se a UF for EX deve ser verificado o conteúdo da **Tag <Cpais>** com o código do país e a **TAG <xpais>** com a descrição do país conforme o exemplo abaixo não gerou ou pode ter gerado como 1058 (Brasil)

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071213613)**

2. Caso não tenha gerado verifique no cadastro de seu **fornecedor ou cliente** os seguintes campos:

A2\_PAIS "Pais" ou A1\_PAIS  PAIS   Exemplo= 023 (Código deve conter três dígitos) :

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070097894)

3. Se já estiver correto será necessário consultar a **tabela SYA e verificar se** para esse país deve estar conforme exemplo abaixo:

SYA -> **YA\_CODGI** = 023 **(com os três primeiros dígitos)**

SYA -> **YA\_SISEXP**= 0230 **(com os quatro dígitos da SISCOMEX)**

**Caso não** esteja como o exemplo acima, este ajuste deve ser realizado **conforme a documentação abaixo:**

[MP- SIGAEIC - Cadasto Sigla Paises tabela SYA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040591674)

4. Caso haja dúvidas do código poderá verificar através do link abaixo:

[SISCOMEX](http://www.bcb.gov.br/rex/Censo2000/port/manual/pais.asp?idpai=CENSOCE)

5. Após isso, **exclua a nota e gere novamente.**

**NT 2022.002** ***Exceção:*** Regra não se aplica quando existir algum item com a UF de consumo do ***combustível igual a exterior (tag: comb/UFCons = “EX”) e com CFOP = “7667*** - Venda de combustível ou lubrificante a consumidor ou usuário final”

Para habilitar a opção de complemento de combustível nos Livros Fiscais, você deverá:  
  
1. Incluir um grupo de produto (**Combustíveis**);

2. Alterar o cadastro do produto e vincular o grupo no campo **B1\_GRUPO;**

3. Informar o grupo no parâmetro **MV\_COMBUS;**

4. Após gerar a nota, acessar: **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos;**

**Na versão 4.00 da NF-e será necessário informar os quatro campos abaixo:  
  
· CD6\_CODANP**

**· CD6\_DESANP**

**. CD6\_UFCONS = EX**

**. CDD\_IFCOMP**

Existe a possibilidade do preenchimento automático dos campos da CD6 para isso usar o ponto de entrada [MATUCOMP](http://tdn.totvs.com/pages/releaseview.action?pageId=6077107)

Existe a possibilidade do campo CDD\_IFCOMP ser preenchido automaticamente. Para isso é necessário ativar o parâmetro MV\_ATUCOMP e usar o ponto de entrada [MATUCOMP](http://tdn.totvs.com/pages/releaseview.action?pageId=6077107)

5. Preencher o CFOP no TES da nota no campo **Cod. Fiscal "F4\_CF" = *7667***

* **Saiba mais:**

Caso a empresa, não utilize o módulo do Sigaeic, foi aberto solicitação de alteração de dicionário e, a partir do próximo release, os campos da tabela SYA, do módulo SIGAEIC, estarão visíveis para todos os módulos.

Para o release atual, será necessário realizar a alteração manual do **menu e a visualização dos campos do módulo SIGAEIC via SIGACFG.**

Detalho como realizar os procedimentos abaixo:

* **Tornando os campos da tabela YA visíveis para todos os módulos**

1. Acesse o módulo SIGACFG, **Base de Dados > Dicionário, Base de Dados**

2. **Empresa > Dicionário de Dados > Pesquisar Lupa**

3. Digite SYA (tabela de países) e clique em Buscar. **Selecione a tabela países e em seguida no ícone para edição.**

4. **Países > Campos > Pesquisar**

5. Preencha a barra de busca com o campo **"YA\_SISEXP" > Editar**

6. Na Aba Módulos, **preencha a checkbox "Utilizado por todos os módulos".** Clique em Salvar.

7. Clique **em Confirmar**

8. **Atualizar base de dados**

9. **Avançar e depois Finalizar**

10. Feche a **rotina SIGACFG.**

 **Adicionando o menu SIGAEIC ao módulo utilizado.**

Acesse o módulo **SIGACFG, Ambiente > Cadastros > Menus**

![SIGAEIC_MENU_1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4402276620055)

Selecione apenas o módulo em que irá **adicionar o menu e confirme.**

![SIGAEIC_MENU_2.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4402273343383)

Selecione o módulo utilizado e clique em Adicionar.

![SIGAEIC_MENU_3.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4402273353495)

Clique em Cadastros, em seguida clique em Novo Item. **Preencha os dados, conforme abaixo:**

* Desc. Portugues/Espanhol/Inglês:  Países

* Programa: EICA100

* Módulo: Easy Import Control

* Tipo: Função Protheus

* Tabelas: SYA

* Status: Habilitado

![SIGAEIC_MENU_4.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4402273365399)

O menu será apresentado em **SIGAFAT > Atualizações > Cadastros > Países**

![SIGAEIC_MENU_5.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4402273372183)

Clique em gerar e preencha com o nome do módulo em que está adicionando o menu e confirme.  **(Exemplo: SIGAFAT)**

Clique em **Fechar e confirme.**

Acesse o módulo que adicionou **o menu (SIGAFAT).**

![SIGAEIC_MENU_6.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4402276649495)

Acesso a rotina realizada com usuário que **não possui acesso ao módulo SIGAEIC** e campos visíveis para edição.

* **Validação da Sefaz:**

![510_rejei__o.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7408001211415)
