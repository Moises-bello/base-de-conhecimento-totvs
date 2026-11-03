---
content_hash: f79e022f13f0db3ae2666d74b629b9800ab2779befa0eaea6d04098e3e7ea598
fetched_at: '2026-06-29T00:08:46.536367+00:00'
page_id: '317301409'
product: rm
source: tdn-rm
title: DT Retorno de Débito Automático em Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317301409
version: 95
---

# Retorno de Débito Automático em Lote

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Retorno de Débito Automático* | **Retorno de Débito Automático** | |
| **Cadastros Iniciais:** | *Bancos e Agências, Convênio, Conta Caixa.* |
| **Parâmetro(s):** | *Contas a Receber | Integração Bancária | Cobrança Eletrônica | Valor Default para diferença em retorno bancário.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-3392> |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | **Oracle e MS-SqlServer** |
| **Tabelas Utilizadas:** | *FBANCOLAYOUT, FBANCO, FLAN, FLANBAIXA, FCXA, FRETORNOBANCARIO, FRETORNOBANCARIOITEM* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Permite efetuar o retorno de débito automático para múltiplos arquivos (Lote), definido por cada coligada/banco.

## Procedimento para Utilização

       1.            Defina no cadastro de perfil o acesso ao Retorno de Débito Automático em Lote.

       2.            Acesse o Retorno de Débito Automático no menu Movimentação Bancária | Integração Bancária | Retorno Bancário | Retorno em Lote e defina os parâmetros

Parâmetros:

* **Banco:** Banco no qual o layout de retorno de débito automático será selecionado
* **Pasta de Leitura dos arquivos de retorno:**  Caminho onde os arquivos de retorno que serão processados deverão estar. Para ambientes que roda em três camadas ou em ambiente CLOUD, é importante selecionar uma caminho no qual o servidor que irá executar o processo e o usuário do sistema operacional tenham acesso de leitura. Serão desconsiderado os arquivo com a extensão .OLD
* **Pasta onde o log de retorno será salvo (opcional):** Caminho onde será salvo os log dos arquivos de retorno processado. Caso não seja informado o log não será salvo. Para ambientes que roda em três camadas ou em ambiente CLOUD, é importante selecionar uma caminho no qual o servidor que irá executar o processo tenha acesso e o usuário do sistema operacional tenham acesso de escrita.
* **Renomear arquivo de retorno processado para extensão .old:** Define se após a execução do processo o arquivo de retorno será renomeado com a extensão .Old. Caso esse parâmetro não seja marcado, então da próxima vez que o processo for executado para pasta selecionada, o sistema irá tentar processa-ló novamente.
* Os demais parâmetros segue a mesma lógica do retorno de Débito Automático, vide help <http://wikihelp.totvs.com.br/WikiHelp/FIN/FIN.RetornoDebitoAutomatico.aspx>

Obs.:

1. A parametrização referente a diferença a maior e a menor será considerada as que foram definidas no parametrizador do menu "Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Receber | Integração Bancária | Cobrança Eletrônica | Valor default para diferença em retorno bancário.
2. A conta caixa que será utilizada para efetuar a baixa será a definida no lançamento.
3. A contabilização será efetuada baseado no evento contábil definido nos default do tipo de documento/campos opcionais do lançamento
4. As pastas onde serão feitas a leitura e gravação do log devem estar compartilhada e deve-se conceder acesso a leitura e gravação.

Abaixo sugestão de como definir a estrutura de pastas:

       3.            Caso esteja em ambiente 3 camadas, será possível definir um agendamento ou a frequência no qual o processo será executado. Com essa funcionalidade o usuário poderá automatizar o retorno de Débito Automático em Lote, tendo que apenas definir um mecanismo para atualizar a pasta de leitura com os arquivos que serão processados.

       4.            Apresentação do Log da execução do processo, mostrando as etapas de processamento, renomear arquivo e salvar o Log (Aba Mensagem)

       5.            Apresentação do Log da execução para cada arquivo arquivo (Aba Logs)

divs
