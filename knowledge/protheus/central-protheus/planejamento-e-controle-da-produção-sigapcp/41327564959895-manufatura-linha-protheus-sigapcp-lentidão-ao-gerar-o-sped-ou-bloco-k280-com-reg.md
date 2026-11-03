---
article_id: 41327564959895
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 21ce8eaae34a5301894040355c4ff9f9bbcab5f4b745975ce93881c50680e367
fetched_at: '2026-06-28T22:42:43.511717+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Lentidão ao gerar o SPED ou Bloco K280
  com registros antigos
type: support-article
updated_at: '2026-06-18T17:48:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41327564959895-Manufatura-Linha-Protheus-SIGAPCP-Lentid%C3%A3o-ao-gerar-o-SPED-ou-Bloco-K280-com-registros-antigos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41327564924439) Tempo aproximado para leitura: 00**:03:22 min**  
  
**Dúvida**  
Ao gerar o **SPED** com o parâmetro **Gerar Bloco K** com o conteúdo 2 - Leiaute Restrito aos Saldos de Estoque está ocorrendo lentidão ou está processando registros antigos no **K280**.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
Essa situação passa a ocorrer nos ambientes que possuem o fonte **MATXSPED** com data superior a 13/03/2026, pois o fonte com esta data possui uma correção na geração do **K280**, listando os estornos de apontamentos de períodos anteriores.  
Sendo assim, para que não liste esses registros e desse modo não comprometa a performance do processo preencha o campo **D3\_PERBLK** com asterisco (\*) para todos os registros que contém o campo **D3\_FILIAL** preenchido com a filial em questão, **D3\_EMISSAO** preenchido com data anterior ao período do qual se deseja gerar o **SPED** e **D3\_PERBLK** em branco ou preenchido com mês e ano do qual se deseja gerar o **SPED**.  
Esse processo faz com que esses registros fiquem marcados na tabela não sendo processados ao gerar o **SPED**, minimizando erros na geração do **K280** e melhorando a performance.  
  
**Exemplo**  
Se o **SPED** que se deseja gerar agora é o de maio de 2026, do grupo 01 e filial 01 e para esse **SPED** está ocorrendo a lentidão ou o registro de dados antigos no **K280**, a instrução **SQL** que pode ser executada é   
**Update SD3010**  
**Set D3\_PERBLK = '\*'**  
**Where**  
**D3\_FILIAL = '01'**  
**and D3\_EMISSAO < '20260501'**  
**and ( D3\_PERBLK = '' or D3\_PERBLK = ' 52026' )**  
  
**Saiba mais**  
Para maiores informações sobre essa manutenção, acesse [K230 não gera K280](https://tdn.totvs.com/pages/releaseview.action?pageId=1050308077)  
  
**Glossário**  
**K280** - Correção de Apontamento - Estoque escriturado  
**K230** - Itens Produzidos  
**D3\_FILIAL** - Filial  
**D3\_EMISSAO** - Data de emissão  
**D3\_PERBLK** - Periodo Bloco K  
**SQL** - *Instructured Query Language*
