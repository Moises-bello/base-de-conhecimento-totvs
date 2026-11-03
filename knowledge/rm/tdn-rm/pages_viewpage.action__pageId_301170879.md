---
content_hash: 5f7c0af14c6585ec61b562a95c96b5212947063256d3c4bb9a8e17a360005002
fetched_at: '2026-06-29T00:08:42.899808+00:00'
page_id: '301170879'
product: rm
source: tdn-rm
title: RMCTB00007_Alteração de Partidas em Grupo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301170879
version: 5
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Alteração de Partidas em Grupo |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do processo:**  Este processo permite que certos dados sejam alterados simultaneamente em várias partidas, de um mesmo lançamento ou de lançamentos distintos, reduzindo bastante o tempo gasto nesta atividade.    **Regras Gerais:**  Os campos mostrados na figura abaixo, são os que podem ser alterados pelo usuário**.**  A opção "Limpar", localizada à frente dos campos Departamento, Centro de Custo, Documento e Contra Partida, quando marcada, limpará, deixando em branco estes campos nas partidas selecionadas.      Abaixo, listamos algumas regras que devem ser levadas em conta pelo usuário na hora de executar o processo:    - Este processo ficará disponível, somente se o usuário tiver permissão em seu perfil para utilizá-lo;  - Partidas de estornos, estornadas ou agrupadas não serão alteradas;  - Partidas selecionadas em lançamentos com diferença entre débitos e créditos os campos Departamento e Filial não poderão ser alterados;  - Quando se altera a Filial, mas não se altera o Departamento, o sistema verifica se os Departamentos informados nas partidas existem na nova Filial. Se não existirem, altera a Filial e limpa os Departamentos. Se existirem, altera a Filial e mantém os Departamentos;  - Quando um departamento é informado deve-se necessariamente informar a Filial correspondente;  - Não será permitida alteração de partidas para Departamentos e Centros de Custo inativos;  - Os parâmetros do sistema que tornam obrigatório o preenchimento do **Centro de Custo**, **Histórico**, **Complemento** e **Documento**, se habilitados, serão observados neste processo, exigindo que se informem estes dados;  - Não será permitido usar Histórico de Fechamento, caso o parâmetro "Permite usar históricos de fechamento em qualquer lançamento" esteja desabilitado;  - Quando o Histórico informado exigir complemento obrigatório será exigido um complemento para processar a alteração;  - Não será permitido alterar partidas que estejam fora do período de lançamentos permitido para o usuário nem que estejam em data anterior à data de fechamento;  - Se o parâmetro do sistema ‘Permite diferenças entre filiais’ estiver desabilitado não será permitido que a alteração de filial gere diferença;  - Só será permitida alteração para uma conta contábil que possui distribuição gerencial se esta conta possuir em seu cadastro o rateio default informado;  - Não será permitido acrescentar uma conta contábil em partidas originadas do RM Nucleus, RM Liber e RM Classis. Partidas com estas origens só poderão ter a conta a débito alterada se na partida original a conta a débito estiver informada, da mesma forma que só poderão ter a conta a crédito alterada se na partida original a conta a crédito estiver informada;    \*Disponível tanto no Lote N quanto no lote Oficial (zero).    **Parametrização Necessária:**  1 - Na visão de lançamento ou do lançamento do lote, selecione qual(is) partidas deverão ser alterada(s), e em seguida acesse o processo:        2 - Informe os campos que serão alterados e clique em OK:        Lembrando que  a opção "Limpar", quando marcada, limpará, deixando em branco estes campos nas partidas selecionadas.    Importante:        3 - Ao fim do processo, é gerado um log, favor avaliar: |
| **Observações:** |  |
