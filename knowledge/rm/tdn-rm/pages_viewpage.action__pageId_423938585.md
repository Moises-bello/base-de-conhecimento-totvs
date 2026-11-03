---
content_hash: 08692b04a9530bbb6e867284efac163a2c1464bb296f454ff927559acb7e081e
fetched_at: '2026-06-29T00:09:27.949772+00:00'
page_id: '423938585'
product: rm
source: tdn-rm
title: Cópia do Mapeamento do Plano de Contas Consolidado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938585
version: 6
---

Versão 12.1.2302

A partir da versão 12.1.2302, o cadastro de "Controladas" será descontinuado do sistema, portanto este processo utilizará o cadastro de Investimentos Societários para buscar investidoras/investidas.  
Para mais informações consulte a documentação a seguir :

Processo só será exibido em coligadas que são investidoras em algum grupo empresarial.  
O processo tem como objetivo copiar, para as coligadas de destino, a associação das contas contábeis do plano de contas paralelo informado pelo usuário.

-Serão copiados os mapeamentos de todas as contas contábeis que possuírem o mesmo código na coligada de destino.   
-As contas que possuírem códigos diferentes serão listadas em um log.   
-Se a coligada de destino possuir mapeamento a cópia não será realizada e uma mensagem informativa será adicionada no log.

A tela possui os seguintes campos:

1. Coligada de Origem: Exibe a investidora (coligada do contexto) e todas as suas investidas, independe do grupo empresarial.
2. Plano de Contas (Capa): Esta opção lista todos os planos de contas paralelos, existentes na coligada corrente, que tenham como finalidade "Consolidação de Saldos".
3. Coligadas de Destino: Exibe a investidora (coligada do contexto) e todas as suas investidas, independe do grupo empresarial, com exceção da coligada de origem previamente selecionada.

Todos os campos acima são obrigatórios.

Veja também

* [Gerar Plano de Contas Paralelo a partir do Plano de Contas Contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=423938681)
