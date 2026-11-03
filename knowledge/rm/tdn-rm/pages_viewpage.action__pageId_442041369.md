---
content_hash: fdb1b4ae5d2cea00f67d620cb4d1473bc679dbb9f32f3c9cdfc29ab8724365e0
fetched_at: '2026-06-29T00:09:53.793982+00:00'
page_id: '442041369'
product: rm
source: tdn-rm
title: DSAUGHCOM-1286 DT Mudança de Leito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=442041369
version: 2
---

# Mudança de Leito

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | Atendimento > Internação > Outros Cadastros > Mudança de Leito |
| **Cadastros Iniciais:** | É necessário ter um Registro de Atendimento |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZMUDANCALEITO |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Tela de Mudança de Leito

## Procedimento para Utilização

      Acessar: Atendimento \ Internação > Outros CAdastros > Mudança de Leito

* Para realizar a mudança do leito, primeiro é necessário localizar o Atendimento através do botão três pontinhos.

* A tela de pesquisa de atendimento será aberta, informe alguns dos dados do atendimento em tela e clique em pesquisar para carregar uma lista dos registros.

* Para confirmar a seleção, selecione o atendimento na lista com um clique e em seguida clique em OK.

* Informe o motivo da transferência.

* Por padrão os campos de Data e Hora da transferência sempre veem preenchidos com a data e hora atuais, caso seja necessário fazer alguma modificação a data e hora não pode ser inferior a data de inicio do antedimento.

* Para selecionar o novo leito, clique no botão e três pontinhos.

* A tela de Controle de Ocupação de Leitos será exibida, para selecionar um novo leito, de um duplo clique sobre o mesmo.

* Depois de selecionado o leito, verificar se haverá necessidade de desmarcar a opção desocupa leito anterior, por padrão essa opção vem sempre marcada.
* Clicar em Avançar para seguir o processo.

* Caso a opção de desocupar estiver marcada e o paciente possuir mais de um leito alocado, será exibida uma listagem de todos os leitos anteriores que serão desocupados.
* Se houver necessidade de manter alguns dos leitos ocupados, basta desmarcar na listagem.
* Clique em avançar.

* A última etapa será solicitado a confirmação para a execução do processo, para confirmar clique em Executar.

Aguarde o seu termino.

Verifique se o processo foi executado com sucesso, e clique em Fechar;

Caso ocorra algum durante o processamento verifique o log de mensagens para tomar as providencias necessárias.

Mudança de leito finalizado.
