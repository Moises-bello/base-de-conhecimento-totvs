---
content_hash: 4b67e11eb1dcf49de8bb4d7beac21972fbaf4f4b0f5477797577572c8db85a4a
fetched_at: '2026-06-29T00:09:28.057283+00:00'
page_id: '423938639'
product: rm
source: tdn-rm
title: Alteração de Partidas em Grupo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938639
version: 4
---

*Atenção!*  
   
Esta funcionalidade só está disponível para as bases já migradas para o Novo Modelo do BackOffice.  
   
Este processo permite que certos dados sejam alterados simultaneamente em várias partidas, de um mesmo lançamento ou de lançamentos distintos, reduzindo bastante o tempo gasto nesta atividade.

Os campos das partidas que poderão ser alterados por este processo são os seguintes: Filial, Departamento, Centro de custo, Documento, Conta Débito, Conta Crédito, Contra Partida, Histórico e Complemento.

Primeiramente devem-se selecionar as partidas a serem alteradas e em seguida informar os novos valores para os campos desejados. Os campos que ficarem em branco não serão alterados, permanecendo com os valores originais.

A opção "Limpar", localizada à frente dos campos Departamento, Centro de Custo, Documento e Contra Partida, quando marcada, limpará, deixando em branco estes campos nas partidas selecionadas.

Ao mandar executar o processo, todas as partidas selecionadas que passarem pelas regras da Alteração de Partidas em grupo terão seus campos alterados com os novos valores aqui informados.

No final do processo será gerado um Log com as informações das alterações efetuadas.

**Regras:**

* Este processo ficará disponível, somente se o usuário tiver permissão em seu perfil para utilizá-lo;
* Partidas de estornos, estornadas ou agrupadas não serão alteradas por este processo;
* Partidas selecionadas em lançamentos com diferença entre débitos e créditos os campos Departamento e Filial não poderão ser alterados;
* Quando se altera a Filial, mas não se altera o Departamento, o sistema verifica se os Departamentos informados nas partidas existem na nova Filial. Se não existirem, altera a Filial e limpa os Departamentos. Se existirem, altera a Filial e mantém os Departamentos;
* Quando se informa um novo Departamento deve-se necessariamente informar a Filial correspondente;
* Não será permitida alteração de partidas para Departamentos e Centros de Custo inativos;
* Os parâmetros do sistema que tornam obrigatório o preenchimento do Centro de Custo, Histórico, Complemento e Documento, se habilitados, serão observados neste processo, exigindo que se informem estes dados;
* Não será permitido usar Histórico de Fechamento, caso o parâmetro "Permite usar históricos de fechamento em qualquer lançamento" esteja desabilitado;
* Quando o Histórico informado exigir complemento obrigatório será exigido um complemento para processar a alteração;
* Não será permitido alterar partidas que estejam fora do período de lançamentos permitido para o usuário nem que estejam em data anterior à data de fechamento;
* Se o parâmetro do sistema 'Permite diferenças entre filiais' estiver desabilitado não será permitido que a alteração de filial gere diferença;
* Só será permitida alteração para uma conta contábil que possui distribuição gerencial se esta conta possuir em seu cadastro o rateio default informado;
* Não será permito acrescentar uma conta contábil em partidas originadas do RM Nucleus, RM Liber e RM Classis. Partidas com estas origens só poderão ter a conta a débito alterada se na partida original a conta a débito estiver informada, da mesma forma que só poderão ter a conta a crédito alterada se na partida original a conta a crédito estiver informada;
* Partidas originadas do módulo financeiro (RM Fluxus) não serão alteradas por este processo;
