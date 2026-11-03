---
article_id: 20463069425303
category: Financeiro
content_hash: 7f86c0daa4c1d17e4e5a8e6e72bbb1561ebfefd4e1101b5cb9af4f514118b2c3
fetched_at: '2026-06-28T22:38:03.129229+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Erro de
  consistência: Dados inconsistentes - 0840'
type: support-article
updated_at: '2024-01-15T19:49:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20463069425303-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Erro-de-consist%C3%AAncia-Dados-inconsistentes-0840
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20463075020951) Tempo aproximado para leitura: **05:00 min****Dúvida**Ao enviar um título via CNAB API o retorno apresentando:

"Erro de consistência: Dados inconsistentes - 0840"

**[![](https://centraldeatendimento.totvs.com/hc/article_attachments/20594372983191)](https://centraldeatendimento.totvs.com/hc/article_attachments/20594372983191)**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FINANCEIRO - A partir 12.1.33  
  
**Solução**

Uma das maiores recorrências, é quando essa mensagem pode estar retornando quando o serviço não está ativo no contrato.

Para confirmação envie um e-mail no canal de suporte do Bradesco:  [suportewebservice@bradesco.com.br](mailto:suportewebservice@bradesco.com.br) 

Informando o retorno "ERRO DE CONSISTENCIA: DADOS INCONSISTENTES - 0840 (6)" e solicite para verificar se o serviço de registro de boletos por webservice está ativo em seu contrato.

Será necessário informar seu CNPJ, número de agência e número da conta. 

Link documentação:  
[Bradesco - Configuração Boletos - FINA710](https://tdn.totvs.com/pages/viewpage.action?pageId=638386427)  
   
Por gentileza validar também o cadastro de banco, por definição do banco Bradesco em sua documentação, a agência deve ser enviada com 4 posições, verifique se esta conforme a documentação abaixo.  
   
[Registro de boletos on-line - Bradesco](https://tdn.totvs.com/display/public/PROT/Registro+de+boletos+on-line+-+Bradesco)  
![](https://totvssuporte.zendesk.com/attachments/token/psIzQbWHEbMfnVrUqLTWvBH5y/?name=image.png)  
   
Caso o cadastro de banco esteja diferente pode realizar o ajuste através do cadastro de parâmetro de banco, aba outros, somente os campos marcados em vermelho. Desta forma não será necessário realizar um novo cadastro de banco.   
   
![](https://totvssuporte.zendesk.com/attachments/token/pURV9PwJRfCxCAe3QOPTbIkuQ/?name=image.png)
