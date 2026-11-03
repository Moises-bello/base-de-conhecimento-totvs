---
content_hash: e7204b69ed36015ee7ef81940dd0d327cc531d694556448590e73d313cb80117
fetched_at: '2026-06-29T00:08:50.256219+00:00'
page_id: '333780271'
product: rm
source: tdn-rm
title: Filtros da Visão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=333780271
version: 12
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

Este documento tem como finalidade, demonstrar o funcionamento do filtro da Visão.

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao clicar no botão novo, uma nova tela é apresentada:

| ID | Nome | Descrição |
| --- | --- | --- |
| **1** | Campo "Pesquisar" | Permite pesquisar a coluna da tabela que será utilizada na condição corrente. |
| **2** | Campo "Colunas" | Apresenta as colunas da tabela associada a visão. |
| **3** | Campo "Operador" | Apresenta todos os indicadores que serão utilizados na condição corrente. |
| **4** | Campo "Valor" | Permite preencher valores referentes à coluna selecionada no campo "Colunas". |
| **5** | Grupo "E/OU" | Inclui as instruções E ou OU entre uma condição e outra. |
| **6** | Botão "Adicionar" | Adiciona uma condição |
| **7** | Botão "Modificar" | Modifica uma condição. |
| **8** | Botão "Novo Grupo" | Permite adicionar um grupo de condições ao filtro. |
| **9** | Ícone "Excluir" | Exclui a condição selecionada. |
| **10** | Ícone "Excluir Todos" | Exclui todas as condições. |
| **11** | Ícone "Voltar uma Posição" | Movimenta a condição selecionada para cima. |
| **12** | Ícone "Avançar uma Posição" | Movimenta a condição selecionada para baixo. |
| **13** | Ícone "Bloqueio" | Permite bloquear uma condição se ser modificada ou excluída. |
| **14** | Ícone "E/OU" | Indica o valor lógico que liga as condições (E/OU) |
| **15** | "Botão Executar" | Inclui ou modifica uma condição e fecha a janela. |
| **16** | "Botão Cancelar" | Fecha a janela de inclusão / modificação de condições. |
| **17** | "Botão Salvar" | Inclui ou modifica uma condição. |

No exemplo abaixo, foi adicionado uma condição:

Código do Turno igual a 1 **[CÓDIGO = 1]**

O Filtro foi salvo com o nome **"Manhã"**.

Aplicando o filtro **Manhã** **[CODIGO = 1],** observe que o apenas o turno **MANHÃ** aparece na visão.

# Aplicando um Filtro Padrão

---

Ao clicar no check **"Sempre usar este filtro ao abrir a visão"**, faz com que o filtro selecionado seja aplicado toda vez que a visão seja aberta, sem necessidade da abertura da tela de filtro.

Atenção

Caso a visão possua um anexo, e esse anexo também tenha sido configurado com o parâmetro de filtro **"Sempre usar este filtro ao abrir a visão"** marcado**,**o filtro não deverá ser aplicado.

**Motivo:** Os **registros das visões anexas** são vinculadas à **um registro da visão mestre**. Internamente, as visões anexas já são filtradas através do registro selecionado na visão mestre, apresentando dados apenas daquele registro.

Observe que a tela de filtro **não é apresentada** ao abrir a **visão anexa**, corroborando com a afirmativa dada acima.

Desde a concepção das **visões anexas**, apesar de estar habilitada a opção **"Sempre usar este filtro ao abrir a visão",** o filtro padrão configurado não é aplicado, devido ao filtro **(originário da visão mestre)** já aplicado à visão anexa.

Mais...

Mais informações sobre .
