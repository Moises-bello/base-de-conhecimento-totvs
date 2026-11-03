---
article_id: 36267191647895
category: Escrita Fiscal - Configurador de Tributos
content_hash: 05e62aaadee41e2c225564d0b4de1d7165fa5ded9539afaea45e3c13fcb8a9c6
fetched_at: '2026-06-28T22:39:17.679022+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - HELP: FWNOWUDTH
  ao incluir Fornecedor em Perfil de Participante'
type: support-article
updated_at: '2025-11-11T21:36:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36267191647895-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-HELP-FWNOWUDTH-ao-incluir-Fornecedor-em-Perfil-de-Participante
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36267208050839) Tempo aproximado para leitura: **00:10 min**  
  
**Ocorrência**  
Ao criar um **perfil de participante** e informar o **código do fornecedor**, o sistema apresenta a mensagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36267208051351)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - A partir da versão 12.1.33  
  
**Causa**  
Essa mensagem ocorre porque há **diferença no tamanho dos campos** relacionados à razão social entre os cadastros:

* **Fornecedor (A2\_NOME)**
* **Participante (F22\_RAZSOC)**

Quando o conteúdo do campo **A2\_NOME** (do fornecedor) possui **quantidade de caracteres maior** do que o campo **F22\_RAZSOC** (no cadastro do participante), o sistema não consegue realizar a cópia automática do nome e apresenta o **HELP: FWNOWUDTH**.  
  
**Solução**  
**Verificar o tamanho dos campos** no dicionário de dados (SX3) para:

* **A2\_NOME**(Fornecedor)
* **F22\_RAZSOC** (Participante)

1. **Ajustar o tamanho do campo** **F22\_RAZSOC** para ser compatível com o **A2\_NOME**, se possível, de acordo com a política de dados da empresa.
2. Caso não seja possível ajustar o tamanho do campo, **editar o nome do fornecedor** de forma que respeite o limite de caracteres do campo **F22\_RAZSOC**.
3. Após o ajuste, repetir a inclusão do perfil de participante.

### **Observação:**

Essa ocorrência não é um erro de sistema, mas uma **validação de consistência** de dados entre cadastros.

**Documentações relacionadas:**

[CFGTRIB - Configurador de Tributos - P12](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+P12)
