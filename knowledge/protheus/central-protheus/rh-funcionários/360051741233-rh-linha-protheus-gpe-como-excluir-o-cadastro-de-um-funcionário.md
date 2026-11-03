---
article_id: 360051741233
category: RH - Funcionários
content_hash: 82cfaf836c4b0ec2467e4c5574dfbc9ac4ee4579f3223ac3ea494d05cdc05817
fetched_at: '2026-06-28T22:43:27.572819+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Como excluir o cadastro de um Funcionário
type: support-article
updated_at: '2025-10-22T18:08:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051741233-RH-Linha-Protheus-GPE-Como-excluir-o-cadastro-de-um-Funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15695735786647) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como **excluir** o cadastro de um Funcionário? 

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução****Antes de prosseguir com a exclusão de um funcionário, é fundamental verificar se há movimentações registradas no Ponto Eletrônico referentes ao período desde sua admissão.**De acordo com as Portarias nº 1510/2009 e nº 671/2021, as marcações originais não podem ser excluídas e devem permanecer armazenadas na base de dados para futuras conferências e auditorias.  
  
Caso sejam identificadas movimentações no Ponto Eletrônico, a rotina **Eliminar Marcações (PONM050)** deve ser executada, seguindo rigorosamente os passos descritos na documentação a seguir:  
[Como utilizar a rotina Eliminar Marcações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007136152-RH-Linha-Protheus-PON-Como-deletar-Marca%C3%A7%C3%B5es-pela-rotina-Eliminar-Marca%C3%A7%C3%B5es)  
  
Após garantir que as movimentações do Ponto Eletrônico foram eliminadas ao funcionário, siga com a exclusão do funcionário, conforme abaixo:  
Para **excluir** o cadastro de um **Funcionário,** acesse o menu **Atualizações > Funcionários > Funcionários:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10838082519703)**

Posicione no registro que precisa excluir, e clique no botão **Outras Ações > Excluir**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079256194)

O sistema emitirá **alertas** de quais tabelas existem informações desta matrícula. Clique em **Sim** para **excluir** os dados e prosseguir:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079260414)

O sistema fará uma varredura em **todas** as tabelas que possuem dados de movimentação, como as de cálculo de Benefícios, Adiantamentos, Férias e Folha:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080379753)

Para emitir o ***log* informativo**, clique em **Sim**:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079262074)

Serão demonstradas no *log* as **tabelas que possuem dados do funcionário que está sendo excluído,** portanto, será necessário que o usuário **exclua primeiramente estes registros para que seja possível prosseguir com a exclusão do Funcionário:**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079262234)

Tabelas que **podem ser apresentadas** para exclusão de relacionamento e como excluir os dados:  
- **NSZ** - Assuntos Jurídicos (módulo 76 - SIGAJURI) - Atualizações > Assuntos Jurídicos > Pesquisas - Excluir vínculo do funcionário na Rotina JURA162   
**- RD0** - Cadastro de Participantes (módulo 53 - SIGAAPD) - Atualizações > Participantes > Cadastro ou digite na lupa de busca no menu APDA020 > selecione o funcionário, clique em Outras Ações > Excluir e confirme  
**- RDZ** - Pessoas x Entidades (módulo 53 - SIGAAPD) - Atualizações > Participantes > Cadastro ou digite na lupa de busca no menu APDA020 > selecione o Funcionário, clique em Outras Ações > Excluir vínculo e confirme  
**- RFV** - Detalhe Memória de Cálculo de Funcionários (módulo 07 SIGAGPE) - Esta tabela não possui rotina para exclusão dos dados, sendo necessário limpar as informações diretamente no banco com referência ao período atual  
**- RGB -** Incidências (módulo 07 - SIGAGPE) - Atualizações > Lançamentos > Por funcionários - selecione o Funcionário, clique em alterar e exclua os lançamentos para ele no período atual  
**- RG1** - Lançamentos Fixos (módulo - 07 SIGAGPE) - Atualizações > Lançamentos > Lançamentos Fixos - selecione o Funcionário, clique em Manutenção e exclua os lançamentos para ele no período atual  
**- SR0 -** Itens de benefício (módulo 07 - SIGAGPE) - Miscelânea > Cálculos > Cancelamento de cálculos -Excluir o cálculo dos roteiros VAL/VRF/VTR  
**- SQG** - Currículo (módulo 20 - SIGARSP) - Atualizações > Candidatos > Currículos > selecione o Currículo correspondente ao Funcionário > Outras Ações > Excluir  
**- SRB** - Dependentes (módulo 07 - SIGAGPE) - Atualizações > Funcionários > Dependentes - selecione o Funcionário, clique em Manutenção e exclua os Dependentes cadastrados  
**- SRE** - Histórico de Transferência (Módulo 07 - SIGAGPE) - Esta tabela não possui rotina para exclusão dos dados, sendo necessário limpar as informações diretamente no banco  
**- SRF** - Programação de Férias (Módulo 07 - SIGAGPE) - Atualizações > Funcionários > Controle de Dias de Direito  
**- TM0** - Ficha Médica (módulo 35 - SIGAMDT) - Atualizações > Atendimento Médico > Ficha Médica - selecione o Funcionário, clique em Outras Ações - Excluir e confirme.

Feito este processo, será apresentado o **cadastro** deste Funcionário. Para concluir a exclusão, clique em **Confirmar:**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079263034)

**Observações:**-A exclusão do cadastro de Funcionário **não integra com o TAF**, mesmo que o evento S-2200 já tenha sido transmitido ao eSocial. Para mais informações acesse [esta documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14616851689495-RH-Linha-Protheus-GPE-eSocial-Exclus%C3%A3o-do-cadastro-de-Funcion%C3%A1rio-no-GPE-n%C3%A3o-integra-com-o-TAF)  
**-**A exclusão só poderá ser feita **dentro do mesmo mês de sua admissão**. Depois que o período de inclusão for fechado, os cálculos realizados para o Funcionário **não podem ser cancelados.**  
  
**Saiba Mais**[RH - Linha Protheus - GPE - A chave (filial/código) não pode ser excluída, pois está sendo utilizada nos arquivos: RD0, RDZ, SPF e SRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041857553-RH-Linha-Protheus-GPE-A-chave-filial-c%C3%B3digo-n%C3%A3o-pode-ser-exclu%C3%ADda-pois-est%C3%A1-sendo-utilizada-nos-arquivos-RD0-RDZ-SPF-e-SRF?source=search)
