---
content_hash: 3b456855695dd11409fd8b6368af2bd846ec27bad5894a91e48ef861184f070d
fetched_at: '2026-06-29T00:08:27.820713+00:00'
page_id: '271646851'
product: rm
source: tdn-rm
title: 298758 MRH-5339 DT Aumento Progressivo em Requisição de Transferência com Alteração
  de Dados Funcionais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271646851
version: 116
---

# AUMENTO PROGRESSIVO EM REQUISIÇÃO DE TRANSFERÊNCIA COM ALTERAÇÃO DE DADOS FUNCIONAIS (ENTRE FILIAIS)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Rotina:** | |  | | --- | | **Rotina** | | Requisição de Transferência com Alteração de Dados Funcionais |  |  | | --- | | **Rotina(s) envolvida(s)** | | Requisição de Transferência com Alteração de Dados Funcionais | | Efetivar Requisição de Transferência com Alteração de Dados Funcionais | | Transferência com Alteração de Dados Funcionais Progressivo | | RM Portal - Requisição de Transferência com Alteração de Dados Funcionais | |
| **Cadastros Iniciais:** | Para a utilização do requisito será necessário parametrizar as requisições de transferências para utilizarem o aumento progressivo. |
| **Tickets relacionados** | 298758 |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Esta implementação visa possibilitar a progressão salarial em requisição de Transferência com Alteração de Dados Funcionais **entre filiais**.

## Importante

 É importante salientar que a transferência entre coligadas não está no escopo desta implementação.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado.

1. Aplique o patch do chamado;

## Procedimento para Configuração

Detalhes para realizar a parametrização estão disponíveis [aqui](http://tdn.totvs.com/display/LRM/DT_Requisicoes_Aumento_Progressivo).

## Procedimento para Utilização

* Acesse Valorização | Requisições | Transferência com Alteração de Dados Funcionais;
* Crie uma nova requisição transferindo um funcionário de filial;
* Coloque um percentual de aumento que extrapole o limite da progressão salarial parametrizado no item acima, Procedimento para Configuração;
* Ao salvar a requisição será exibida a mensagem da imagem abaixo e clicando em sim a progressão será criada automaticamente com base nos limites parametrizados;

* Prossiga com a requisição até que a mesma esteja aprovada;
* Acesse Valorização | Efetivações | Efetivar Transferência c/ Alteração de Dados Funcionais;
* Abra o anexo Transferência com Alteração de Dados Funcionais Progressivos e selecione a requisição aprovada anteriormente;
* Note que é necessário a rescisão do funcionário.
* E que por tal motivo os aumentos do funcionário estão pendentes;
* Realize a rescisão do funcionário no RMLabore;
* Após realizada a rescisão o ícone irá mudar para Progressão Pendente, caso a progressão possua mais de um step;
* Caso só possua um step a requisição já ficará concluída e não será necessário avançar o step, pois ele será avançado no processo de rescisão;
* Verifique que o primeiro aumento foi efetivado e que ainda existe um step da progressão pendente;
* Para avançar o próximo step do aumento progressivo acesse Valorização | Efetivações | Efetivar Transferência c/ Alteração de Dados Funcionais | Anexo | Transferência com Alteração de Dados Funcionais Progressivo;
* Selecione a progressão pendente e vá em Processos | Efetivar transferência com alteração de dados funcionais progressivo;
* A requisição ficará concluída após avançar o último step da progressão;

## 

## Criando uma requisição pelo RMPortal

* A Requisição de Transferência com Alteração de Dados Funcionais também poderá ser criada no RMPortal;
* Acesse o RMPortal | Recursos Humanos | Requisições;
* Crie uma nova requisição de Transferência com Alteração de Dados Funcionais realizando transferência entre filiais;
* Ao salvar a requisição a mesma irá para o próximo aprovador;
* Ao logar no RMPortal com o usuário do próximo aprovador note que o botão ‘Aumento Progressivo’ estará habilitado, clique no mesmo e vá em ‘Sugerir Progressões’.
* Neste caso foi sugerido uma progressão de 60%, e foi criado os seguintes aumentos progressivos que totalizam 60%.
* Avance a etapa e aprove a requisição;
* Após a aprovação da requisição os próximos passos serão os mesmos descritos acima para a requisição que foi aberta no RM.exe;

**Observação:**

Não é possível utilizar a progressão salarial entre coligadas diferentes.
