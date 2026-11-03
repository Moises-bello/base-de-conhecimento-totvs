---
content_hash: 831db764c6104ef763110923994b6648fc72404e56d9139cd846d8d7fe47d096
fetched_at: '2026-06-29T00:09:28.659793+00:00'
page_id: '423938741'
product: rm
source: tdn-rm
title: Plano de Contas Consolidado 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938741
version: 3
---

O plano de contas consolidado é necessário para representar a soma das contas contábeis das empresas presentes no conglomerado econômico, nele as contas contábeis de controladas e controladora serão associadas de forma com que cada conta seja representada por uma conta do plano de contas consolidado.

O cadastro deste plano de contas pode ser feito através do plano de contas paralelo, para isso, basta o usuário informar no campo "Instituição Responsável / Finalidade" a finalidade (Consolidação de Saldos) presente no cadastro do plano de contas paralelo. Feito isso, o sistema entende que esse é o plano de contas consolidado que terá as suas contas representas no registro K200.

Após a criação do plano de contas consolidado, o usuário precisa cadastrar as contas contábeis que fará parte deste plano, é importante que seja cadastro um plano de contas para atender todas as empresas que participam do conglomerado econômico, pois as contas contábeis de todas as empresas envolvidas serão vinculadas a sua respectiva conta consolidada.  
    
**Vinculo das contas**  
As contas contábeis das controladas e da controladora precisam ser vinculadas as contas do plano de contas consolidado, para isso o usuário deve acessar cada controlada/controladora (através das coligadas) e realizar o vinculo manualmente, conta a conta.

Quando o plano de contas paralelo for do tipo (Consolidação de Saldos) ele poderá ser acessado em todas as coligadas do sistema, isso justamente para que controladas e controladora possa realizar o vinculo de suas contas contábeis a conta consolidada.

Importante: Instituições que utilizam plano de contas global, é necessário realizar o vínculo apenas para uma empresa, pois como o plano de contas é o mesmo para as demais empresas do conglomerado econômico, não há necessidade de demais vínculos.

Após realizado o vinculo das contas é necessário que seja executado um processo que irá realizar a soma dos saldos das contas contábeis, o resultado dessa soma será o saldo da respectiva conta consolidada, essas informações serão salvas em banco de dados na tabela CSALDOCONSOLIDAO. Vale ressaltar que podem haver eliminações que deverão ser eliminadas dos saldos das contas, caso haja eliminações o processo gera os saldos já eliminando do saldo da conta consolidada tal valor.  
   
Observação  
Foi disponibilizado para o usuário, através dos anexos do cadastro do plano de contas paralelo (Finalidade: Consolidação de Saldos) a opção "Saldo das Contas do Plano de Contas Consolidado" essa opção permite consultar os saldos que foram gerados pelo processo. 

Veja Também

* Cadastro de Controladas
* K100 - Código do País
* [Cálculo Saldo Consolidado](http://tdn.totvs.com.br/pages/viewpage.action?pageId=423938856)
* [Eventos societários](http://tdn.totvs.com/x/U6sEGw)
