---
content_hash: 3fbed7b831a0d5ceab953c4307ec5dc413933907eaa4fea1691462d31dcd4768
fetched_at: '2026-06-29T00:08:39.860713+00:00'
page_id: '286022824'
product: rm
source: tdn-rm
title: DT Sinais Vitais x Unidade de Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Sinais+Vitais+x+Unidade+de+Atendimento
version: 106
---

# Sinais Vitais x Unidade de Atendimento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Cadastros/Cuidados com o Paciente/Prescrição Médica/Itens da Enfermagem | |
| **Tickets relacionados** | [Ticket #875326](https://totvssuporte.zendesk.com/agent/tickets/875326 "Open ticket in Zendesk Support") |
| **Requisito** | [SAUHRM02-1245](http://jiraproducao.totvs.com.br/browse/SAUHRM02-1245) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Tabelas Utilizadas:** | SZPEPENFUNIDATEND |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementado cadastro que permite que o usuário vincule um sinal vital à uma unidade de atendimento, indicando se será ou não padrão para ela.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realize a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.18 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.18.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.18

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

**Vincular Unidade de Atendimento com os Itens de Enfermagem**

1. Acesse **Cadastros/Cuidados com o Paciente/Prescrição Médica/Itens da Enfermagem**.
2. A tela de Itens de Lançamento (Itens da Enfermagem) abrirá. Clique em **Incluir**, ou se preferir, é possível editar um item existente clicando em **Editar** (os passos descritos a seguir podem ser executados em ambos os caso).

        3. Para a aba de **Unidade de Atendimento** ficar habilitada é necessário:

            a. O cadastro utilizar Prontuário Eletrônico do Paciente.

            b. Um dos seguintes Tipos de Itens estar selecionado: Equipamento, Procedimento, Insumo, Prescrição de Enfermagem, Itens p/ registro médico, Parâmetro Hemodinâmicos, Parâmetros Ventilatórios, Outros parâmetros de monitorização, Sinais Vitais e Insulina.

          4. A aba **Unidade de Atendimento** não será exibida se um dos seguintes Tipos de Item estiver selecionado: Ganho Parenteral, Ganho Enteral, Perda, Perda Insensível, Hemoderivado, Para troca de plantão de enfermagem, Imunização, Problemas, Diagnósticos Próteses/Implantes, Medicamentos Gases Ventilações, Itens p/ registro de inf. Cirúrgica.

          5. Na aba **Unidade de Atendimento**, clique em **Incluir**.

Observação

Certifique-se que a Descrição e o Tipo Item foram informados na aba Identificação, caso contrário não será possível incluir uma unidade de atendimento.

          6. É possível selecionar mais de uma unidade, clique em **OK** para incluir.

         7. As unidades de atendimento ficarão pré cadastradas.

         8. Para editar uma unidade de atendimento clique em **Editar**, é possível definir se a unidade será padrão.

       9. Defina a unidade para Padrão ou desmarque a opção conforme sua necessidade:

       10. Note que agora a unidade deixou de ser padrão:

      11. Para salvar todas as modificações na aba **Unidade de Atendimento** clique em **Salvar**.

divs
