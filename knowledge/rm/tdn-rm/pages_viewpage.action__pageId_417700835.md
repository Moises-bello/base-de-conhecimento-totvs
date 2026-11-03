---
content_hash: 25a166bcd2ee7c750ac377f08c2d569637ef951defa1285f0aa070e73e694cd5
fetched_at: '2026-06-29T00:09:12.867124+00:00'
page_id: '417700835'
product: rm
source: tdn-rm
title: 'S-2299/S-2399 - Como gerar Retificação de desligamento?(Parâmentro: Não lançar
  Liquido de retificação no envelope da competência Atual desmarcado)'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=417700835
version: 41
---

false

**A partir das Versões:**

* **12.1.22**
* **12.1.23**
* **12.1.24**

# Objetivo:

---

       O objetivo deste documento é trazer informações de como é o processo de retificação de desligamento, mostrando desde a parametrização até o seu cancelamento.

---

13Retificação gerada pelo Cálculo de Rescisão ComplementarRetificação gerada pelo Cálculo de Rescisão Complementar21Execução do scriptExecução do script

Para a liberação do menu de retificação de rescisão, na versão 12.1.22 será necessário executar o script "Retificação de Folha" através do sistema RM.Atualizador.exe.

3-1ParametrizaçãoParametrização

Acesse o menu Serviços Globais| Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em acesso aos menus e permita o acesso 02.01.05.09 Retificação da Folha de Pagamento

Acesse o menu RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 5/7

Cadastre o período inicial que será apresentado na tela do processo de rescisão complementar.

Cadastre os eventos com os novos código de calculo conforme necessidade.

[382 - Estorno Base IRRF Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718661) 

[383 - Líquido Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718720) 

[384 - Pagamento Líquido Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718780)

385 - Base IRRF Retificação 

[386 - Pensão Alimentícia Judicial Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718807) 

[392 - Estorno Base IRRF 13 Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465178948) 

[393 - Base IRRF 13 Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465178458)

[402 -](http://tdn.totvs.com.br/pages/viewpage.action?pageId=461921386)[Estorno Base IRRF Férias Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465179595)

[403 - Base IRRF Férias Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465179614)

[404 -](http://tdn.totvs.com.br/pages/viewpage.action?pageId=461921386)[Estorno Base IRRF Partic. Lucros Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465179628)

[405 - Base IRRF Partic. Lucros Retificação](https://tdn.totvs.com.br/pages/viewpage.action?pageId=465179659)

[406 -](http://tdn.totvs.com.br/pages/viewpage.action?pageId=461921386)[Pensão Alimentícia Férias Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465179669)

[407 -](http://tdn.totvs.com.br/pages/viewpage.action?pageId=461921386)[Pensão Alimentícia 13° Salário Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465179681)

[408 - Pensão Alimentícia Partic. Lucros Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465179696)

[424 -Valor Pensão Alimenticia Judicial Retificação](https://tdn.totvs.com.br/pages/viewpage.action?pageId=519725850)

[425 -Valor Pensão Alimenticia Férias Retificação](https://tdn.totvs.com.br/pages/viewpage.action?pageId=519725867)

[426 -Valor Pensão Alimenticia 13º Salário Retificação](https://tdn.totvs.com.br/pages/viewpage.action?pageId=519725880)

[427 - Valor Pensão Alimenticia Partic Lucros Retificação](https://tdn.totvs.com.br/pages/viewpage.action?pageId=519725884)

3-2CalculoCalculoCalculotrue3-1CalculoCalculo

Na rescisão complementar marque o parâmetro “Retificar rescisão”. A “Data de Último Movimento” e o parâmetro “Pagamento de verbas de natureza salarial ou não salarial devidas após o desligamento” ficarão desabilitados quando o parâmetro “Retificar rescisão” estiver marcado. Escolha o período de lançamento que será gravado no mês competência da rescisão, ou seja, será inserido novo período no mesmo mês em que a rescisão original foi calculada. Este período será por default o período selecionado no parametrizador (Parametrizador / eSocial / Configurações / Configurações 5/7).

**Observação:**

* A diferença entre outras verbas de natureza salarial ou não salarial devidas após o desligamento e a retificação da rescisão é que na primeira o evento será devido por exemplo na apuração de comissão após a rescisão e no segundo foi alguma verba paga incorretamente e deve ser retificada.
* Quando ocorrer uma rescisão por dissidio sim e uma retificação de rescisão no mês competência, deverá ser lançado o calculo em períodos diferentes.

O parâmetro “Período sequencial” deverá ser utilizado quando tem várias retificações em períodos diferentes. Marcando este parâmetro o sistema busca o maior período existente com retificação calculada e lança no período posterior.

Cadastre o(s) evento(s) que deseja incluir ou alterar no período selecionado. Os eventos informados devem ser aqueles que se quer retificar. 

**Exemplo:**

Supondo que a competência atual está em Dezembro, foi paga uma rescisão em outubro, porém foi devido uma diferença para esse funcionário.

Lançado no envelope de pagamento do mês da rescisão no período 10000

Lançado no envelope atual:

Após executar o processo de cálculo parametrizando conforme acima será gerado um gatilho do evento S-2299 – Desligamento no período de apuração do período original como retificação do envio anterior;

Também será gerado o gatilho para retificar também o evento S-1210 - Pagamentos de Rendimentos do Trabalho no mês de apuração referente ao mês de pagamento da rescisão original

O XML S-1200 gerado na competência atual é gerado com a TAG tpAcConv =  F, visto que, conforme o layout do eSocial somente é permitido pagamentos após a demissão do funcionário desta maneira.

O XML S-1210 gerado na competência atual é gerado com a TAG tpPgto = 1 pois está relacionado ao S-1200 gerado no item acima.

3-2Calculo - Marcando o parâmetro "Calcular Somente Eventos Informados"Calculo - Marcando o parâmetro "Calcular Somente Eventos Informados"

Na rescisão complementar quando é marcado o parâmetro “Calcular Somente Eventos Informados”, somente será calculado este evento que foi digitado.

.

**Observação:**

* A diferença entre outras verbas de natureza salarial ou não salarial devidas após o desligamento e a retificação da rescisão é que na primeira o evento será devido por exemplo na apuração de valores que influenciam no recálculo da rescisão e no segundo foi alguma verba paga incorretamente e deve ser retificada

Marcar “Retificar rescisão” e escolher o período de lançamento que será gravado no mês competência do fator gerador da rescisão, ou seja, será inserido novo período no mesmo mês em que a rescisão original foi calculada antes da rescisão complementar. Este período será por default o período selecionado no parametrizador anteriormente.

O parâmetro “Período sequencial” deverá ser utilizado quando tem várias retificações em períodos diferentes. Marcando este parâmetro o sistema busca o maior período existente com retificação calculada e lança no período posterior.

**Exemplo:**

Supondo que competência atual está em novembro, foi paga uma rescisão em setembro e ficou faltando o lançamento de um evento.

Lançado no envelope de pagamento do mês da rescisão no período 10000

Lançado no envelope atual:

Após executar o processo de cálculo parametrizando conforme acima será gerado um gatilho do evento S-2299 – Desligamento no período de apuração do período original como retificação do envio anterior;

Também será gerado o gatilho para retificar também o evento S-1210 - Pagamentos de Rendimentos do Trabalho no mês de apuração referente ao mês de pagamento da rescisão original

O XML S-1200 gerado na competência atual é gerado com a TAG tpAcConv =  F, visto que, conforme o layout do eSocial somente é permitido pagamentos após a demissão do funcionário desta maneira.

O XML S-1210 gerado na competência atual é gerado com a TAG tpPgto = 1 pois está relacionado ao S-1200 gerado no item acima.

3-3CancelamentoCancelamento

Para o cancelamento da retificação da rescisão é necessário primeiramente cancelar o período atual onde foram lançados os valores dos líquidos da retificação.

Após o cancelamento do período atual, marque o parâmetro "Retificação folha/rescisão",  selecione o período em que foi lançada a retificação da rescisão e informe a competência e o período que se quer cancelar.
