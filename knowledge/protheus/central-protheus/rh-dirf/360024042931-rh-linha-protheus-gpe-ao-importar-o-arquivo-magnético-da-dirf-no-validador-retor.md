---
article_id: 360024042931
category: RH – DIRF
content_hash: da0e583d22f311ef415cb66d3ed1225ac10d3af8a7fcdc191466b3f479c6e1d4
fetched_at: '2026-06-28T22:44:06.781926+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao importar o arquivo magnético da DIRF no validador
  retorna mensagem: REGISTRO INFPA RELAÇÃO DEPENDÊNCIA NÃO INFORMADA'
type: support-article
updated_at: '2025-08-06T20:52:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024042931-RH-Linha-Protheus-GPE-Ao-importar-o-arquivo-magn%C3%A9tico-da-DIRF-no-validador-retorna-mensagem-REGISTRO-INFPA-RELA%C3%87%C3%83O-DEPEND%C3%8ANCIA-N%C3%83O-INFORMADA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33999061052951) Tempo aproximado para leitura: 00:01:00 min**

**Ocorrência**Ao importar o arquivo magnético da DIRF no validador, retorna mensagem: REGISTRO INFPA RELAÇÃO DEPENDÊNCIA NÃO INFORMADA:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21026632756503)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões.  
  
**Causa**  
Campo Relação de dependência no cadastro de Beneficiários não esta preenchido.  
  
**Solução**Esta mensagem trata-se de um AVISO e não é impeditiva para a entrega da **DIRF**, pois o campo Relação de dependência não é um campo obrigatório na **DIRF**, conforme leiaute abaixo  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9204728562071)

Para cadastrar a relação de dependência para os beneficiários na DIRF, na rotina de **Beneficiários**, pelo caminho **>Atualizações >Funcionários >Beneficiário**s, localize o funcionário do beneficiário em questão e preencha o campo abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9204707296279)  
  
Após alteração, execute novamente a rotina Gerar Arquivo para a matricula, assim ao gerar o arquivo magnético a informação será gerada.

**Saiba Mais**  
[RH - Linha Protheus - GPE - Passo a Passo para gerar dados/gerar Arquivo DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437012)
