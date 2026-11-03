---
article_id: 360035197933
category: TAF - GIA
content_hash: 648cd277fd1fe42898b843f5259b47114a616ccc9ed0b7f20976b981cef3d6db
fetched_at: '2026-06-28T22:41:32.357534+00:00'
product: protheus
section_id: 1500001547982
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GIA-SP - 5º
  Passo - Processamento
type: support-article
updated_at: '2024-06-04T19:11:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035197933-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GIA-SP-5%C2%BA-Passo-Processamento
---

**Ocorrência**

Necessário atualizar o ambiente TAF para utilização da GIA-SP.

**Ambiente**Protheus - Livros Fiscais – A partir da versão 12.1.17]  
 **Causa**Necessidade das configurações para a geração do arquivo da **Nova GIA**através do **TAF.**  
 **Solução**Execução da rotina de Processamento - **TAF -> Miscelânea -> Integração -> Processamentos (TAFAINTEG).**  
  
Nesta rotina será a onde ele irá integrar tudo que veio da tabela TAFST1 para as tabelas oficiais do TAF, o procedimento que ele irá realizar será o seguinte, as informações da tabela TAFST1 ele irá alimentar a tabela TAFST2 (JOB 0) e posteriormente alimentar a TAFST2 e as tabelas oficiais do TAF (JOB 2).

OBS:  O extrator fiscal, a partir do mês 03/2020, gera os dados diretamente na **TAFST2** para clientes que utilizam o TAF como módulo. A TAFST1 não é utilizada na integração de clientes que usam o Protheus e TAF como módulo do Protheus.

Dessa forma, as opções "Limpar TAFST1" e "Transferir da TAFST1 para TAFST2" ficarão desabilitadas nesse cenário. Deve ser marcado somente  "Transferir da TAFST2 para o TAF".  
  
Selecione somente as opções, conforme imagem abaixo e clique em **Confirmar**.   
![](https://tdn.totvs.com/download/attachments/379308197/image2019-8-21_14-55-0.png?version=1&modificationDate=1566410102443&api=v2)
