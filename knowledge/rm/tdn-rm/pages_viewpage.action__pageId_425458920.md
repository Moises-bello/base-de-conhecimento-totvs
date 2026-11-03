---
content_hash: 6f9da15869fba06306e36ada76009c6ebc82b298a55400cc3a65e70bebd9a0e7
fetched_at: '2026-06-29T00:09:32.785595+00:00'
page_id: '425458920'
product: rm
source: tdn-rm
title: Integração Protheus e Processo Seletivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458920
version: 3
---

Para ocorrer a integração de lançamentos gerados do Processo Seletivo com o Protheus é necessário realizar os seguintes passos:

**1- Parametrização da conexão de seu banco de dados Corpore com o banco de dados Protheus**.

Localização: Parâmetros do sistema\ Integração.  Este parâmetro tem por finalidade indicar em qual base encontra-se as tabelas do Protheus. É imprescindível que seja configurado, visto que a integração não funciona sem esta parametrização.

Informa-se os seguintes campos: Servidor de integração, Base de dados, Usuário e Senha. Após informar estes campos o botão de teste de conexão verificará a disponibilidade de acesso a base de dados apontada. Estas configurações terão validade por cada filial dentro da coligada.

**2-** **Configurações financeiras de integração do Processo Seletivo**.   
 Localização: Cadastro de processo seletivo / Anexo Integração Protheus.  Este anexo destina-se ao preenchimento dos dados financeiros necessários para a integração referentes a cada processo seletivo.  
 Configura-se os campos:  Item contábil, Classe de valor, Prefixo e Código da natureza financeira.

Estes dados serão gravados na tabela 'SPSPROCSELINTPROTHEUS'. O sistema realizará internamente um processamento de atualização e exportação dos dados de lançamentos gerados ou alterados pelo Processo Seletivo.

As seguintes funcionalidades trabalham com lançamentos:

-   

-   

-  

**Como e quando ocorre a integração?**

A importação dos dados será realizado logo após o processamento de lançamentos na integração com o RM Fluxus (TOTVS Financeiro).  
 Para a integração entre os sistemas, os status disponíveis na tabela INT\_TITULO no campo TIT\_STATUSIMPORT são:

**1-** Em processamento (Executado o segundo passo de importação)

**2-** Base do Protheus com os dados sincronizados com sucesso.

**3-** Houve erro durante a sincronização dos dados.

**4-** Em processamento (Executado o primeiro passo de importação)

**Executado o primeiro passo de importação**:

Logo após a geração ou alteração do lançamento no RM Fluxus e registro na FLAN, um registro de lançamento é criado na INT\_TITULO. Este registro é preenchido com os valores de lançamento gerado no Fluxus, sendo os dados principais:   
 Código da coligada Filial ID do lançamento Nome do cliente Valor Número do documento Tipo Data de vencimento Desconto Multa/Dia Multa Juros Juros/Dia Moeda  
 Após esta atualização, o registro da INT\_TITULO estará com o campo TIT\_STATUSIMPORT com valor "4".

**Dica**: Para localizar o lançamento na INT\_TITULO, busque por  TIT\_IDLAN = :IDLAN

**Executado o segundo passo de importação:**

Consiste em atualizar a INT\_TITULO com os dados financeiros configuráveis para cada processo seletivo. Para tal, os campos gravados na tabela 'SPSPROCSELINTPROTHEUS' serão recuperados e atualizados no registro de lançamento criado na INT\_TITULO.

Lançamentos gerados pelos serviços: Processo de alterar forma de inscrição, Geração de inscrições anônimas, Inscrição da área ofertada.  
 Campos atualizados (De Processo Seletivo Para Protheus):

Item contábil       

De: SPSPROCSELINTPROTHEUS.IDITEMCONTABIL (Base Corpore)

Para: INT\_TITULO.TIT\_ITEMCONTABIL (Base Protheus)

Classe de valor  

De:  SPSPROCSELINTPROTHEUS.IDCLASSEVALOR (Base Corpore)

Para: INT\_TITULO.TIT\_CLASSEVALOR (Base Protheus)

Prefixo

De:  SPSPROCSELINTPROTHEUS.IDPREFIXO (Base Corpore)

Para: INT\_TITULO.TIT\_PREFIXO (Base Protheus)

Código da natureza financeira

De: SPSPROCSELINTPROTHEUS.IDNATUREZA (Base Corpore)

Para: INT\_TITULO.TIT\_NATUREZA(Base Protheus)

Além destes campos serão atualizados:  
 Processo Seletivo (TIT\_PROCEL) Número de inscrição (TIT\_NUMEROINSC)  
 Após esta atualização, o registro da INT\_TITULO estará com o campo TIT\_STATUSIMPORT com valor "1".  Por fim, um "gatilho" na base do Protheus está configurado para recuperar os lançamentos com TIT\_STATUSIMPORT com valor "1", importá-los e, caso obtenha **sucesso**, atualizar o TIT\_STATUSIMPORT para o valor "2". Se haja algum problema o valor será "3".
