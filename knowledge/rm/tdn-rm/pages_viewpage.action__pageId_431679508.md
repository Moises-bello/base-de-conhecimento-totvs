---
content_hash: 629b972f301d9a93744040c67947936ec4c6262b01ba871d5ea2b89694d0db4d
fetched_at: '2026-06-29T00:09:42.611503+00:00'
page_id: '431679508'
product: rm
source: tdn-rm
title: Geração de Guias Automaticamente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=431679508
version: 28
---

#f5f5f5#363636noneGeração de guias automaticamente

## **Conteúdo**

**2Conteúdononenone**

## **01. Visão Geral**

Este processo proporciona uma solução eficiente para geração de guias de pagamento de impostos no Módulo Fiscal. Simplificando as operações, ele visa otimizar a experiência do usuário ao oferecer uma abordagem automatizada e precisa para o cumprimento das obrigações fiscais. Explore este recurso para uma gestão ágil e eficaz dos pagamentos de impostos no seu ambiente fiscal.

## **02. Geração de Guias****automáticas**

GuiasTributos de Origem Financeira

Para os tributos que são apurados considerando Lançamentos Financeiros, utilize o processo "Geração de Guias a partir de Lançamentos Financeiros" que está visível no período de apuração destes tributos.

Aviso

Para as empresas que transmitem a EFD-Reinf, a apuração será realizada na DCTFWeb e por este motivo orientamos que faça o procedimento na DCTFWeb e em seguida gere a fatura diretamente no Financeiro não sendo mais necessário executar este processo no Fiscal. Para mais detalhes consulte o documento

Aviso de uso da EFD-Reinf

**Tela de Aviso:**

O aviso será apresentando apenas quando estiver preenchido o campo "URL de conexão" nos Parâmetros do Fiscal | Integração | EFD-REINF por Filial.

Tributos de Origem Fiscal

Para os tributos que são apurados considerando os Lançamentos Ficais, utilize o menu Processos | Geração de Guias automaticamente. 

### **ICMS e ICMS ST**

O Processo de Geração de Guias ICMS-ST:

1 - Guias do ICMS Antecipado:

* O sistema deve permitir gerar as guias com o Período de Apuração aberto. Isto é necessário porque as guias devem ser geradas à medida que as notas são emitidas e não somente após o encerramento do período.
* Devem ser selecionados apenas Lançamentos Fiscais de **entrada**, cuja Situação da Retenção do ICMS ST da Regra de ICMS associada ao CFOP esteja marcado como "**Antecipação**" e que já não tenha guia GNR associada.
* O lançamento que tiver sua guia gerada deve ser "marcado" para que não sejam geradas guias em duplicidade (DLAFGUIA)

2 - Guias do ICMS Substituto Tributário

* As guias referente à substituição tributária (Situação da Retenção do ICMS ST da Regra de ICMS associada ao CFOP esteja marcado como "**Substituto Tributário**") precisam ser geradas após o encerramento do Período de Apuração.
* Devem ser selecionados apenas Lançamentos Fiscais de **saída**, cuja Situação da Retenção do ICMS ST da Regra de ICMS associada ao CFOP esteja marcado como "**Substituto Tributário**".

## **03. Tributos que não geram Guias Automáticas**

Para os tributos IOF, OUTROS, ISS ST CONTRATANTE, ISS ST SUBCONTRATANTE, CPMF, RET E DARF não é possível inserir Guias automaticamente, visto que são de caráter específico. Logo, estas guias devem ser incluídas manualmente.

## **04**. **Como identificar a guia Automática?**

Através do campo Forma de geração, no Cadastro de Guias é possível identificar se ela foi incluída de forma Automática ou Manual.

Evite duplicidade

Se em um determinado período de apuração houver geração de Guias DARF automaticamente, a inclusão manual de DARF ficará comprometida. Com isso, há duas possibilidades: ou a inclusão de todas as guias deve ser feita manualmente, ou todas as guias devem ser geradas automaticamente. Para consultar as guias geradas, acesse os Anexos do Período | Guias DARF.
