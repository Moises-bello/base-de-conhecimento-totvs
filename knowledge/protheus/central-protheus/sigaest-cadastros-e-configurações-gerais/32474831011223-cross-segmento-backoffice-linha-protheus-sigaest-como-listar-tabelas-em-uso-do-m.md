---
article_id: 32474831011223
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 027f626f05fb171b7b628131920f17984dcaee681cb774b370a0289de6c4cc82
fetched_at: '2026-06-28T22:39:08.159403+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como Listar Tabelas
  em uso do Módulo Estoque/Custos?
type: support-article
updated_at: '2025-05-30T14:54:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32474831011223-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-Listar-Tabelas-em-uso-do-M%C3%B3dulo-Estoque-Custos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32474854663063) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Quais são as tabelas vinculadas ao modulo de Estoque Custos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

**Objetivo:**  
Este boletim tem como finalidade orientar sobre como identificar as tabelas relacionadas ao módulo do Protheus, com foco especial no módulo **Estoque/Custos (SIGAEST – Módulo 4)**.

### **Consulta via Tabela SX2 (Tabela de Dados)**

Para obter a relação de tabelas vinculadas a um módulo específico, utilize a tabela **SX2**, filtrando pelo campo `X2_MODULO`, conforme o número do módulo desejado, dessa forma você tera uma relação das tabelas em uso para aquele determinado modulo.

> **Exemplo:**  
> Módulo Estoque/Custos (SIGAEST) → `X2_MODULO = '4'`

#### Exemplo de consulta SQL:

`SELECT * FROM SX2010 WHERE X2_MODULO = '4' AND D_E_L_E_T_ = ' '`

> **Observação:** No exemplo acima, `'010'` representa o código da empresa. Altere conforme sua base.

Para mais informações sobre a estrutura da SX2, consulte a documentação oficial TOTVS da area de Framework:

[SX2 – Tabelas de Dados (TDN)](https://tdn.totvs.com/display/public/framework/SX2+-+Tabelas+de+Dados)

### **Importante**

* Este boletim é voltado principalmente para clientes que desejam identificar as tabelas do módulo **Estoque/Custos (SIGAEST – Módulo 4) em uso**, seja para fins de **customização**, **integração** ou **análises técnicas**.
* A mesma lógica pode ser aplicada para identificação de tabelas em **outros módulos**, bastando substituir o número correspondente no campo `X2_MODULO`.
* Em caso de dúvidas sobre as tabelas de módulos específicos, orientamos entrar em contato diretamente com a equipe responsável pelo respectivo módulo.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Estoque Custos*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001533821-Estoque-e-Custos-SIGAEST)
