---
article_id: 9787103463063
category: eSocial - Tabelas/Não Periódicos
content_hash: e93ec0c2167dc42a878129bad8a99a21b772a7b7303ecf09c3b865fa6c43e62d
fetched_at: '2026-06-28T22:47:10.433960+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na validação do campo ''aliqRat'': Para Alíquota
  RAT diferente de 1, 2 e 3 deve ser informado um processo judicial'
type: support-article
updated_at: '2024-12-18T15:45:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9787103463063-RH-RM-FOP-eSocial-Erro-na-valida%C3%A7%C3%A3o-do-campo-aliqRat-Para-Al%C3%ADquota-RAT-diferente-de-1-2-e-3-deve-ser-informado-um-processo-judicial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24166748170775) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao gerar o evento S-1005 é apresentada a seguinte mensagem **Erro na validação do campo 'aliqRat': Para Alíquota RAT diferente de 1, 2 e 3 deve ser informado um processo judicial.****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro é apresentado ao gerar o S-1005 cujo no cadastro do CEI ou Seção não está informado e também pode ocorrer quando a alíquota RAT não correspondem aos valores 1, 2 ou 3.

**Solução**Para correção da ocorrência favor realizar as validações abaixo:  
**• Utiliza Tomadores de Serviços**1. No cadastro do **Cliente/Fornecedor** acesse **Anexos | eSocial;**2. Preencha o campo **Aliq. RAT** ou se o parâmetro **Considera dados da filial no cadastro de cliente fornecedor** estiver marcado estiver;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9990592381591)

3. Irá recuperar valor do campo **%Acid. Trabalho** da seção correspondente a filial informada neste cadastro.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9987806465047)**

**• CEI do Cliente/Fornecedor**1. No cadastro do Cliente/Fornecedor acesse a aba **CEI do Cliente | Fornecedor**, clique em **Anexos | eSocial;**2. Preencha o campo **Aliq. RAT**ou se o parâmetro **Considera dados da filial no cadastro de cliente fornecedor** estiver marcado, irá recuperar valor do campo **%Acid. Trabalho** da seção correspondente a filial informada neste cadastro;

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9990707782935)

3. Após gere o XML novamente e envie ao eSocial.  
  
**•  Não utiliza tomadores de serviço**1. O sistema buscará da seção vinculada ao funcionário. Para isso, acesse **Administração de Pessoal | Seção | Dados p/INSS** e preencha o campo **%Acid. Trabalho;**

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9990856280727)**

2. Em seguida, gere o XML e envie ao eSocial.

**Observação**Em caso de **alíquotas RAT** diferentes de 1, 2 e 3, deverá vincular um **[Processo Judicial.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008847432-RH-RM-FOP-eSocial-Cadastro-do-evento-S-1070-Tabela-de-Processos-Administrativos-Judiciais)**Para cadastrar o Processo Judicial, acesse **Administração de Pessoal | Seção | eSocial** e vincule o processo desejado.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9990951789079)

2. Em seguida, gere o XML na Fila de Eventos e envie ao eSocial.  
  
**Saiba mais**

[- Obras: S-1005 x S-1020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008581451-RH-RM-FOP-eSocial-Obras-S-1005-x-S-1020)
