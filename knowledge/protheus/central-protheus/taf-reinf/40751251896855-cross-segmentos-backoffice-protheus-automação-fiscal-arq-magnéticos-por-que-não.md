---
article_id: 40751251896855
category: TAF - REINF
content_hash: 26e80f14db95b45c35dd019aa074f5ed98faf9b6097e4085c7d584221b9a0e65
fetched_at: '2026-06-28T22:41:33.313244+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Automação Fiscal - Arq. Magnéticos
  -   Por que não é listado as notas fiscais na consulta do evento da rotina TAFA635?
type: support-article
updated_at: '2026-05-27T11:52:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40751251896855-Cross-Segmentos-Backoffice-Protheus-Automa%C3%A7%C3%A3o-Fiscal-Arq-Magn%C3%A9ticos-Por-que-n%C3%A3o-%C3%A9-listado-as-notas-fiscais-na-consulta-do-evento-da-rotina-TAFA635
---

**Dúvida**  
  Por que não é listado as notas fiscais na consulta do evento da rotina TAFA635.

![nenhum dado encontrado.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40751251879447)  
  
**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - A partir da versão **12.1.2410**  
  
**Solução**

   Para que um documento seja habilitado e listado para transmissão no Monitor de Eventos (rotina TAFA635), ele deve atender a critérios específicos de integração. Caso um documento não seja exibido na rotina, é necessário revisar os dados gravados nas tabelas ***C20, C30 e C35*** do TAF.

**Validações Necessárias**

Siga o checklist abaixo para garantir que a nota atenda aos requisitos do monitor:

* **Tabela C20 (Cabeçalho do Documento):**

  + **Regra:** O documento deve ser obrigatoriamente do **Modelo 55** (NF-e).
  + **Validação:** Verifique se o campo de modelo do documento (C20\_CODMOD) está preenchido com o valor 00029.
* **Tabela C30 (Itens do Documento):**

  + **Regra:** As informações complementares do XML precisam estar detalhadas.
  + **Validação:** Confirme o preenchimento obrigatório dos campos de item (C30\_ITEXML), quantidade (C30\_QTDXML) e unidade de medida (C30\_UMXML).
* **Tabela C35 (Tributos do Item):**

  + **Regra:** Apenas documentos contendo tributos da Reforma Tributária (**IBS e/ou CBS**) são considerados nesta rotina.
  + **Validação:**  O campo de código do tributo (C35\_CODTRI) deve possuir um valor válido, respeitando o cadastro existente na tabela C3S.

![MOnitor C3S.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40751251882135)

### Integração de Notas de Débito e Crédito (Evento 211128)

Para que operações de nota de débito ou crédito (evento 211128) sejam processadas corretamente, existe uma relação de dependência obrigatória.

> **Atenção:** O documento complementar não será integrado ao TAF (e não aparecerá no Monitor de Eventos) se a **nota principal (original)** não constar previamente no sistema. Certifique-se de que a nota de origem já está integrada ao TAF antes de processar o documento complementar.

   
  **IMPORTANTE: A rotina para integração das informações do monitor é o TSI, o extrator fiscal não integra dados como IBS e CBS e o complemento do XML**

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Como configurar o TSI (TAF Service Integration)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4424759792151-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-configurar-o-TSI-TAF-Service-Integration)  
  
Documentação complementar: <https://tdn.totvs.com/display/public/TAF/Monitor+de+Eventos+-+TAF+-+P12>  
    
Ambiente deve estar atualizado:

**Release:**

**12.1.2410:**<https://suporte.totvs.com/portal/p/10098/download?e=1174332>

**12.1.2510:**<https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1228187>

**LIB:**

**Harpia:**<https://suporte.totvs.com/portal/p/10098/download?e=1050526>

**Onça:**<https://suporte.totvs.com/portal/p/10098/download?e=1168735>
