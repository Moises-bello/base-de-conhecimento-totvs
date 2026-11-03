---
article_id: 30086170599575
category: Gestão de Transportes (TMS)
content_hash: a177a238f01d159631e33b0467d4d42e5e7089a1d316e222d9b54abb26631579
fetched_at: '2026-06-28T22:45:33.449570+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Valor do Frete Zerado no cálculo do frete
  a receber
type: support-article
updated_at: '2025-03-14T14:25:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30086170599575-Log%C3%ADstica-Linha-Protheus-TMS-Valor-do-Frete-Zerado-no-c%C3%A1lculo-do-frete-a-receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30086144236439) Tempo aproximado para leitura: **00:04:20 min** **Dúvida**Como corrigir a mensagem **Valor do Frete Zerado** no cálculo do frete a receber?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**A mensagem **Valor do Frete Zerado** ocorre no calculo do frete a receber quando o Sistema não encontra os dados necessários para realizar o cálculo do frete.   
Essa mensagem, sem detalhes sobre qual componente de cálculo não encontrou valores, aparece quando, no cadastro da **Configuração da Tabela de Frete - TMSA130**, todos os componentes de frete estão configurados como **Não obrigatórios**.  
  
Sendo assim, a primeira dica para identificar o problema é acessar o cadastro da **Configuração da Tabela de Frete - TMSA130** e alterar todos os componentes de fretes para **obrigatórios,** através do campo **Comp.Obrig. -** **DVE\_COMOBR** **= Sim** em cada um dos componentes. Desta forma, ao calcular o frete novamente, teremos, no *help* detalhado, a indicação do componente de frete que apresentou a falha de cálculo.   
É importante reforçar que não é necessário manter os componentes como obrigatórios para o cálculo, essa é apenas uma dica para facilitar o diagnóstico do problema.  
  
Para que o cálculo do frete ocorra corretamente, devemos identificar qual cadastro está incorreto ou qual informação falta ou não se enquadra na **Entrada do Documento do Cliente - TMSA050**. Para isso, devemos revisar os seguintes cadastros:

1. Se o componente indicado no *help* calcular sobre o peso da mercadoria **DT3\_TIPFAI = 01**, valide se o campo **DTC\_PESO** **- Peso** foi preenchido na nota fiscal do cliente na **Entrada Documento de Cliente****- TMSA050** ou se o peso preenchido enquadra-se nas faixas da tabela de frete.
2. Se o componente indicado no *help* calcular sobre valor informado **DT3\_TIPFAI = 07**, é necessário que na digitação da **Entrada do documento do cliente - TMSA050**, seja preenchido a quantidade desejada desse componente em **Outras Ações/ Valor Informado**. Também é necessário que a quantidade preenchida enquadra-se nas faixas da tabela de frete.
3. Caso o parâmetro **MV\_CALNORI** esteja habilitado, o Sistema estará apto a verificar os níveis superiores da região origem no cálculo do frete, para buscar a **Tabela de Frete** configurada para as regiões de níveis superiores, como **Filial, Estado ou País**. Neste caso, verifique em **Componente de frete - TMSA030** se o componente informado no *help* está configurado com o campo **Pesquisa Taxa - DT3\_PSQTXA** como **Sim**, isso permitirá que o componente também faça a verificação de níveis superiores de região.
4. Caso o parâmetro **MV\_CALNORI** esteja desabilitado, o Sistema não fará a busca de regiões superiores para a região de origem. Neste caos, verifique o cadastro da **Tabela de Frete - TMSA010** para garantir que ela possua as mesmas regiões de origem e cálculo que foram utilizadas na digitação da **Entrada Documento de Cliente - TMSA050** e se os valores para o componente em questão foram configurados na tabela de frete.   
   Caso a tabela de frete não exista, inclua uma nova tabela de frete para essas regiões específicas e configure os valores de frete para o componente de frete informado no *help*.
5. Verifique no cadastro de **Estrutura de Regiões - TMSA120** se as regiões de origem e de cálculo fazem parte da estrutura.
6. Verifique se o cadastro do **Contrato Cliente - TECA250** possui a tabela de frete vinculada ao serviço utilizado na **Entrada Documento de Cliente****- TMSA050**

**Saiba mais**Para mais informações acesse:  
[Configuração da Tabela de Frete (TMSA130 - SIGATMS)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=471943831)  
[Tabela de Frete (TMSA010 - SIGATMS)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=484684997)   
[Componentes de Frete (TMSA030 - SIGATMS)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=471937653)  
[Logística - Linha Protheus - TMS - Frete Informado para Frete a Receber](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027399631-Log%C3%ADstica-Linha-Protheus-TMS-Frete-Informado-para-Frete-a-Receber)  
[Logística - Linha Protheus - TMS - Valor Informado no Frete a Receber](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051098734-Log%C3%ADstica-Linha-Protheus-TMS-Valor-Informado-no-Frete-a-Receber)  
[Logística - Linha Protheus - TMS - Subfaixa Tabela de Frete](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051926213-Log%C3%ADstica-Linha-Protheus-TMS-Subfaixa-Tabela-de-Frete)
