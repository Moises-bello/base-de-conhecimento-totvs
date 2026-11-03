---
article_id: 360028967531
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: a42e2d57164bd051c22223b046f798a9df56b4ceba19862fab175394ab0885f0
fetched_at: '2026-06-28T22:42:05.230136+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Nova Apuração e Geração do Arquivo (FISA001 e FISA008)
type: support-article
updated_at: '2023-04-14T17:35:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028967531-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Nova-Apura%C3%A7%C3%A3o-e-Gera%C3%A7%C3%A3o-do-Arquivo-FISA001-e-FISA008
---

**Dúvida**EFD Contribuições - Nova apuração e geração do arquivo (FISA001 e FISA008) **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Com objetivo de oferecer uma melhor ferramenta de processamento e conferência, foi desenvolvida a nova rotina de apuração de PIS e COFINS, chamada “Apuração EFD Contribuições” (**FISA001**). Esta nova apuração trata as regras de cálculos presentes na EFD Contribuições, ou seja, irá processar PIS e COFINS considerando todas as regras disponíveis no guia prático do EFD Contribuições. Os valores processados de PIS e COFINS serão também contabilizados e terão seus títulos correspondentes gerados no módulo financeiro.

Com a implementação da rotina **FISA001**, teremos então no ERP duas apurações de PIS e COFINS, **MATA996** que não atende as regras da EFD e a **FISA001** que atende as regras, por este motivo informamos que a rotina **MATA996** será substituída pela nova apuração **FISA001**, sendo assim não serão mais realizadas manutenções e/ou correções na rotina **MATA996** a partir de **30/04/2015**. A rotina permanecerá disponível no ERP, porém não receberá nenhuma atualização/ajuste a partir desta data. Por este motivo orientamos a utilização da **FISA001** para processamento dos valores de PIS e COFINS e não mais **MATA996**.

A atual rotina geradora do EFD-Contribuições (**SPEDPISCOF**) também foi substituída, pois agora a geração da EFD é baseada na apuração de PIS e COFINS (**FISA001**). A nova rotina é a **FISA008**, e a partir de **31/10/2015** não efetuaremos manutenção no programa **SPEDPISCOF**, ou seja, não realizaremos mais atualizações da legislação nem correções de não conformidade na rotina antiga, a manutenção irá seguir atuando no programa **FISA008**.

Os relatórios abaixo também foram descontinuados e substituídos pelo relatório de conferência da EFD Contribuições (**FISR101**), portanto, não serão mais realizadas manutenções e/ou correções nestas rotinas:

 

* **MATR906 - Relatório Pis/Cofins.**
* **MATR946 - Extrato Pis/Cofins.**
* **MATR927 - Crédito de Pis/Cofins na depreciação do Ativo Imobilizado.**

Abaixo link contendo as informações acima e artigos relacionados a apuração do PIS e COFINS nas rotinas FISA001 e FISA008.

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/9995225390743-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Boletim-t%C3%A9cnico-Apura%C3%A7%C3%A3o-e-gera%C3%A7%C3%A3o-arquivo-txt-EFD-Contribui%C3%A7%C3%B5es?source=search>
