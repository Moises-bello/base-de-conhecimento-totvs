---
article_id: 360027494872
category: Escrita Fiscal - Impostos - Cálculos
content_hash: b37da328e6026a8d66247aa1858ca4015c4a9ab54abacd2450320ded72c03cf6
fetched_at: '2026-06-28T22:39:30.644492+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Acertos Fiscais -
  Rotina MATA900
type: support-article
updated_at: '2022-04-26T13:48:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027494872-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Acertos-Fiscais-Rotina-MATA900
---

**Dúvida**Procedimentos de utilização da rotina de Acertos Fiscais - Rotina MATA900.   
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Por meio da rotina de Acertos Fiscais por item (MATA900), é possível alterar valores registrados no Livro Fiscal (SF3) e Itens do Documento (SFT ), porém não retratando as movimentações de origem.  
Este procedimento afeta algumas obrigações acessórias, por exemplo: Sintegra, GIA, etc. Por este motivo, alerta o usuário, em mensagem na tela, sobre possíveis riscos/danos nesse processo, se não utilizados com prudência.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4474333127191/mceclip0.png)

A rotina de Acertos Fiscais tem o intuito de permitir ajustes quanto a informações de escrituração fiscal no documento.   
  
**1.** Acesse o módulo Livros Fiscais, opção Miscelâneas/ Acertos/ Acertos fiscais (MATA900).  
**2.** Selecione a opção Por item.  
**3.** Altere as notas fiscais desejadas e confirme.  
  
O Sistema apresenta a mensagem de possível alteração nos demais procedimentos do Sistema.  
  
**4.** Certifique-se da movimentação e confirme. A partir desse momento, é possível acertar manualmente o Livro Fiscal (SF3)/ Livro Fiscal por item (SFT).  
  
**5.** Selecione a nota fiscal desejada.  
  
**6.** Selecionada a nota, clique no botão **Outras Ações** e selecione a opção **Por item**.  
  
**7.** Será apresentada nova tela, na qual é possível alterar valores escriturados no Livro Fiscal (SF3) e Livro Fiscal por Item (SFT), lembrando que somente o CFOP e a Data de Entrada são retratados até a origem, ou seja, na nota fiscal, os demais campos alterados serão gravados somente nos Livros Fiscais e estarão divergentes da notas fiscais originais.  
  
**8.** A opção Considerar no reprocessamento? no topo da tela, determina se a nota fiscal selecionada deve ser considerada no reprocessamento. Quando a opção for “Sim”, excluirá os Livros Fiscais para as notas fiscais do período, gerando novos registros de Livro Fiscal nas tabelas SF3 e SFT, eliminando as manutenções efetuadas anteriormente.  
  
**9.** Ainda no primeiro quadro são apresentados os campos-chave escriturados no Livro Fiscal (SF3) que devem ser replicados no Livro Fiscal por item (SFT), cujos campos são apresentados na primeira planilha. Já os valores dos campos CFOP, Código de Serviço, Observação, etc., da tabela SF3 devem ser transportados para todos os itens da tabela (SFT) correspondente, relacionado pelo campo de identificação Ident. SFT.  
  
**10.** Na segunda planilha estão aos valores escriturados por item de nota fiscal que devem ser aglutinados no Livro Fiscal (SF3), de acordo com a “quebra” desse livro, por meio do campo de identificação Ident. SF3.  
  
**11.** Realizadas as alterações, é possível visualizá-las por meio da pasta Resumo, que relaciona os campos alterados em sequência, conforme segue:  
· Item/Campo  
Determina qual linha foi alterada.  
É possível constatar que o campo CFOP foi alterado.  
· Campo  
Determina qual campo sofreu alteração, o campo de CFOP foi alterado.  
· Seq.  
Determina quantas vezes este campo foi alterado.  
· Vlr. Anterior/Vlr. Atual  
Estes campos relacionam o conteúdo anterior e posterior à alteração.  
  
**12.** Confirmadas as alterações, os valores de registro do livro fiscal serão alterados e gravados, conforme manutenção de acerto fiscal.  
  
**13.** O campo “Espécie” só poderá ser alterado por meio da opção Alterar, e a informação da Espécie será replicada para a tela Por Item e salva nas tabelas SF3 E SFT

**Tabelas utilizadas:**

SA1 – Cadastro de Clientes;   
SA2 – Cadastro de Fornecedores;   
SF3 – Livro Fiscal;   
SFT – Livro Fiscal por item;   
SF1 – Cabeçalho de nota fiscal de entrada;   
SD1 – Itens de nota fiscal de entrada;   
SF2 – Cabeçalho de notas fiscais de saída;   
SD2 – Itens de nota fiscal de saída  
  
**Rotinas envolvidas:**   
  
Acertos Fiscais (MATA900)
