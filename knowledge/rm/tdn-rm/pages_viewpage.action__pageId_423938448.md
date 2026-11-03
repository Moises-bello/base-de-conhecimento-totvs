---
content_hash: d0dd334df73f419c92569b638fd4add194e172c77eb70ce3af21abf8f5717787
fetched_at: '2026-06-29T00:09:27.167849+00:00'
page_id: '423938448'
product: rm
source: tdn-rm
title: Geração de Movimento por Indicador do Período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938448
version: 2
---

O processo de geração de movimento para indicadores de uso do objeto de manutenção permite que sejam gerados movimentos para indicadores de uso de objetos de manutenção que estejam alocados em projetos cadastrados no sistema TOTVS Obras e Projetos. Através dessa funcionalidade é possível cobrar a locação de acordo com os indicadores de uso lançados para o objeto durante o período em que o mesmo esteve alocado.

**Parametrização**

Para ter acesso a esta funcionalidade, primeiramente o usuário deverá ter permissão a este processo nas tags de segurança do sistema TOTVS Manutenção.   
A permissão é dad acessando o menu Cadastros | Segurança | Perfis, selecionando o perfil que está vinculado ao usuário, e acessando a aba "Acesso a menus".  
Após dar permissão ao usuário é necessário acessar o menu Ambiente | Parâmetros | Manutenção, aba movimento e marcar o parâmetro "Gera Movimento para Histórico do Indicador".   
Ao marcar esse parâmetro a aba "Parâmetros para Geração do Movimento" é habilitada no cadastro de Tipo de Objeto de Manutenção.  
Na aba Parâmetros para Geração do Movimento é necessário parametrizar alguns dados como o indicador de uso que será usado na geração do movimento.   
Será necessário também cadastrar um produto ou serviço para que o mesmo seja incluído no movimento que irá gerar os cálculos dos valores para cobrança do indicador.   
Após cadastrar o produto/serviço é necessário informar o preço que será usado como base para o calculo do movimento.  
***Atenção!***: O produto informado nessa aba deverá obrigatoriamente ter a mesma unidade de controle do indicador de uso que será usado na geração do movimento, exemplo, se o indicador usado no objeto de manutenção é Quilometro, a unidade de controle do produto deverá também ser Quilometro.

**Processo**

Existem duas maneiras de gerar movimento para o indicador. O primeiro é acessando o cadastro de objeto de manutenção, clicar em processo e depois em "Geração de Movimento por Indicador por Período".   
Acessando esse caminho o usuário deverá informar o movimento que será utilizado na geração, o projeto (cadastrado no sistema TOTVS Obras e Projetos), a tarefa e as datas iniciais e finais. O movimento será gerado para os indicadores que estiverem dentro do período informado nas datas  
A outra maneira de gerar o movimento para o indicador é acessando o histórico de indicador de uso do objeto e clicar em processo "Geração de movimento por indicador selecionado", dessa maneira é gerado o movimento para todos os indicadores selecionados e não por um período de datas como mostrado anteriormente.  
***Observação***: Não é possível gerar mais de um movimento por indicador de modo que se o usuário selecionar um indicador que já contenha um movimento gerado o sistema emitirá uma mensagem informando ao usuário que a geração do movimento não é possível.  
Após selecionar um objeto de manutenção para a geração de movimento é necessário certificar-se de que o centro de custo e a filial do objeto são os mesmos do projeto que se deseja gerar o movimento, do contrário o projeto não ficará visível para seleção e a geração do movimento não será concluída, ou seja, o objeto deverá possuir o mesmo centro de custo e filial do projeto.
