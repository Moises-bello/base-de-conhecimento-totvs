---
article_id: 360021184172
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 0df43c6388355e3d614159c9bc2f45cd3da9891bfe9e86cb18024d746e66871e
fetched_at: '2026-06-28T22:42:07.920132+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T082
  Código de Atividade C5M_CODATI inexistente
type: support-article
updated_at: '2022-08-18T17:45:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021184172-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T082-C%C3%B3digo-de-Atividade-C5M-CODATI-inexistente
---

**Ocorrência**Erro 1 - Linha: 1 - O valor '84842000' informado na coluna 5 para o campo Código de Atividade ( C5M\_CODATI ) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, quando o código de serviço utilizado não existe na tabela **C5V-Códigos de Atividades da Receita Bruta**.

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Informe um código de atividade válido para o item utilizado;   
2. Limpe o conteúdo do parâmetro **MV\_VAUTCON** e execute a Wizard de Configuração novamente;   
3. Execute o Extrator Fiscal novamente e Processamento.
