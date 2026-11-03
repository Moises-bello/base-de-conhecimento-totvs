---
content_hash: 8fd53209301454383771644808db53d58ec808af4265b8890f9783fc6e50b621
fetched_at: '2026-06-29T00:09:52.908889+00:00'
page_id: '439700196'
product: rm
source: tdn-rm
title: FISCAL01-7057 SPED Fiscal - Registro C191(FECP)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439700196
version: 2
---

# Registro C191(FECP)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | TOTVS Gestão Fiscal |
| **Módulo:** | Gestão Fiscal |
| **Função:** | SPED Fiscal |
| **Situação/Requisito:** | **Registro C191: INFORMAÇÕES DO FUNDO DE COMBATE À POBREZA – FCP – NA NF-e (CÓDIGO 55)**  Inclusão do registro C191 com a seguinte estrutura:    Um Registro para cada C190. Nível hierárquico 4. |
| **Solução/Implementação:** | A geração do Registro C191 foi implementada para ser gerada a partir dos dados de FECP no  Lançamento com as seguintes restrições:   * VL\_FCP\_OP – Só pode ser preenchido quando o campo CST\_ICMS do registro C190 assumir o valor **x00,x10,x20,x51,x70 ou x90.** * VL\_FCP\_ST – Só pode ser preenchido quando o campo CST\_ICMS do registro C190 assumir o valor **x10, x30, x70, x90, 201, 202, 203 ou 900**. * VL\_FCP\_RET – Só pode ser preenchido quando o campo CST\_ICMS do registro C190 assumir o valor **x60 ou 500**. * A geração do Registro C191 está sujeita aos Modelos de Documento 55. * Quando os valores do FECP Estado de Destino e o FECP Próprio estão zerados o Registro C191 não é gerado * O cálculo do Registro é feito prioritariamente por Item, caso não exista Itens no Lançamento o cálculo é feito por Situação Tributária.    ATENÇÃO A geração do Registro C191 acontecerá para Lançamentos feitos a partir de 2019. |
