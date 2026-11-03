---
content_hash: 6fefe493c8179416303b70c8baa10c7595d78c671a18fbed7ea5597a58442122
fetched_at: '2026-06-29T00:08:09.082796+00:00'
page_id: '239022809'
product: rm
source: tdn-rm
title: TURKSM_DT_Atualização_Preço_x_Volume_MATMED
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=239022809
version: 116
---

# Preço de MATMEDs multiplicados pelo volume quando unidade de medida de estoque difere da unidade de medida de prescrição

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | **Utilitários RM Saúde / Importação de Tabelas de MATMED de Convênios** |  |  | | --- | | **Rotina(s) envolvida(s)** | | **Estoques / Produto / Informações TOTVS Saúde / Tabela de Preço** | |
| **Cadastros Iniciais:** | **Estoques / Produto / Informações TOTVS Saúde / Tabela de Preço** |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER e ORACLE |
| **Tabelas Utilizadas:** | SZITEMESTQPRECO, TPRODUTODEF |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Realizada alteração no sistema, para que o preço do item a ser atualizado seja multiplicado pelo volume, quando a unidade de medida utilizada pelo estoque difere da unidade de medida utilizada para prescrever o item para pacientes.

## Procedimento para Utilização

1. Acesse **Utilitários / Utilitários RM Saúde / Importação de Tabelas de MATMED de Convênios**.
2. Selecione a tabela básica e clique em "**Importar**".
3. Selecione a planilha de valores e clique em "**Importar**".
4. Neste exemplo, digitamos seu valor como “1”, clicamos com o botão direito sobre o item e clicamos em “Relacionar e Atualizar Preço”. Nota: O valor “1” é preenchido, simulando que o convênio passe o valor do próprio ML (como sempre faz) e não o valor do frasco.
5. Selecione o produto que deseja relacionar e clique em "**OK**".
6. Ao gravar com sucesso, acesse o cadastro do produto, **anexo "Informações - TOTVS Saúde" / anexo "Tabela de Preço",** selecione a tabela básica e veja que o preço do item é o valor informado na rotina anterior multiplicado pelo volume.

   **\***Foi realizada esta alteração pois quando a **unidade de medida importada difere da unidade controlada pelo estoque**, é necessário **atualizar o PREÇO multiplicando pelo VOLUME**, do contrário, ao lançar este item na conta de um paciente o **fator de conversão** fará com que o preço fique errado. **observação: fator de conversão é definido pelo VOLUME.**

divs
