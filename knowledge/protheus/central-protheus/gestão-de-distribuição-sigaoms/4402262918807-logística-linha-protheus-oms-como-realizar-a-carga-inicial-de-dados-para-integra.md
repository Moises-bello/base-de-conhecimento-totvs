---
article_id: 4402262918807
category: Gestão de Distribuição (SIGAOMS)
content_hash: 5229dcfd43c17bbe4fcd596e413acfe151659ab7cae61ed9bfd97b85e7e103c1
fetched_at: '2026-06-28T22:45:49.731916+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como realizar a Carga inicial de dados para
  integrar o TOTVS OMS x TOL/TRE
type: support-article
updated_at: '2022-10-20T14:07:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402262918807-Log%C3%ADstica-Linha-Protheus-OMS-Como-realizar-a-Carga-inicial-de-dados-para-integrar-o-TOTVS-OMS-x-TOL-TRE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:06:24 min**  
**Dúvida**Como realizar a **Carga inicial de dados** para integrar o **TOTVS OMS** x **TOL/TRE**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Os cadastros devem ser realizados no **TOTVS OMS** e integrados ao **TOL/TRE**.  
  
A ativação da integração, não impede a **inclusão**, **alteração** e **exclusão** de registros no **TOL/TRE**, mas esse procedimento não é recomendado, pois as operações realizadas sobre os cadastros no **TOL/TRE** não são replicadas para os respectivos cadastros no **Protheus**.  
  
Apenas as operações de **inclusão** e **alteração** são **consideradas na integração e são efetuadas sempre que ocorrerem, desde que parametrizadas para serem on-line**.  
A operação de **eliminação** sobre os registros de cadastros não é integrada, pois não é possível verificar a integridade referencial no Sistema de destino para considerá-la como restrição de eliminação dos registros no **Protheus**.  
  
O sucesso das operações de inclusão e alteração de registros pode ser verificado acessando o programa de consulta no menu do **TOL/TRE** em: **Interface - Log**.  
O Sistema de origem dos dados não recebe o **status do processamento dos registros enviados**, por isso, considera integrado com base apenas na **confirmação de recepção da mensagem de integração**.

Para realizar a carga inicial, e replicar os cadastros de **Empresas-Filiais**, **Clientes**, **Produtos**, **Tipos de Veículos**, **Fornecedores** e **Transportadoras** para o **TOL/TRE**, deve ser realizado o procedimento abaixo:

* No **TOTVS OMS**, acesse **Atualizações/Cockpit Logístico/Parâmetros Integração - OMSXCPL1**.  
  Preencha os parâmetros conforme instruções do artigo [Logística - Linha Protheus - OMS - Parâmetros para integrar o TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402272406551)
* Utilize a opção **Ações relacionadas/outras ações** para testar a conexão com o **WebService**.
* Caso apareça a mensagem **Não foi possível conectar no WebService**, copie a **URL** e cole em algum navegador de internet e verifique se o **WebService** está acessível.
* Clique em **Confirmar** para gravar os parâmetros.
* Acesse **Atualizações/Cockpit Logístico/Carga de Dados - OMSXCPL2**.
* Marque os cadastros desejados e clique em processar.
* Se desejar, posicione na lista de cadastros o item e utilize o **botão Filtro**, para aplicar um filtro de seleção de registros na tabela.
* O filtro padrão do programa só permite que **registros da filial** em que o **usuário está logado** seja enviado ao **TOL/TRE**.
* No caso de **falha de envio** por meio do **botão Falhas**, é possível realizar uma consulta dos registros que apresentaram alguma falha no envio.
* Posicione o cursor sobre o **registro de falha** que deseja verificar e selecione a opção **Visualizar**, o programa irá apresentar o possível erro.
* Após o acerto do cadastro, posicione sobre o registro com falha e selecione a opção **Reenviar**.
* Após o processamento, clique em **Sair** para finalizar o programa.
* Após a carga inicial, os cadastros de **clientes**, **produtos**, **tipos de veículos**, **fornecedor** e **transportadora**, no **TOTVS OMS** devem ser feitos normalmente e desde que a integração esteja ativa, os dados serão replicados automaticamente ao **TOL/TRE**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402269493015/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402274992663/mceclip2.png)

**Fluxo das Informações**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402271160087/mceclip4.png)

**Filiais****Tipo de Fluxo**: **TOTVS OMS x TOL/TRE**.  
**Mensagem**: **LocalityAcquisitionService**  
O envio de **empresas-filiais** **não é automático**, ou seja, ao cadastrar no **Protheus** uma nova empresa-filial, para que essas informações sejam replicadas para ao **TOL/TRE** é necessário executar a carga de dados disponível em: **Atualizações/Cockpit Logístico/Carga de Dados - OMSXCPL2**, assinalando a opção **SM0 - Cadastro de Filiais**.  
Os dados serão enviados ao **TOL/TRE** por meio do método **updateLocalities**.  
Esses dados, por sua vez, serão salvos como **localidade** e poderão ser visualizados no **TOL/TRE** em: **Cadastro - Localidades.**  
**Clientes**  
**Tipo de Fluxo**: **TOTVS OMS x TOL/TRE**.  
**Mensagem**: **LocalityAcquisitionService**  
Ao cadastrar um **cliente** no **Protheus**, quando a integração estiver ativa os dados serão enviados ao **TOL/TRE** por meio do método **updateLocalities**.  
Esses dados, por sua vez, serão salvos como **localidade** e poderão ser visualizados no **TOL/TRE** em: **Cadastro - Localidades.  
  
Fornecedores**  
**Tipo de Fluxo**: **TOTVS OMS x TOL/TRE**.  
**Mensagem**: **LocalityAcquisitionService** ou **CarrierAcquisitionService**  
Ao cadastrar um **fornecedor** no **Protheus**, quando a integração estiver ativa os dados serão enviados ao **TOL/TRE** por meio do método **updateLocalities,** conforme parametrização do cadastro tabela **SA2**, de acordo com o comentado acima.  
Esses dados, por sua vez, serão salvos como **localidade** e poderão ser visualizados no **TOL/TRE** em: **Cadastro - Localidades.**  
**Transportadores**  
**Tipo de Fluxo**: **TOTVS OMS x TOL/TRE**.  
**Mensagem**: **CarrierAcquisitionService**  
Ao cadastrar um **transportador** no **Protheus**, quando a integração estiver ativa os dados serão enviados ao **TOL/TRE** por meio do método **CarrierAcquisitionService**.  
Esses dados, por sua vez, serão salvos como transportadoras e poderão ser visualizados no **TOL/TRE** em: **Cadastro - Transportadoras.  
  
Produtos**  
**Tipo de Fluxo**: **TOTVS OMS x TOL/TRE**.  
**Mensagem**: **ProductAcquisitionService**  
Ao cadastrar um **produto** no **Protheus**, quando a integração estiver ativa os dados serão enviados ao **TOL/TRE** por meio do método **ProductAcquisitionService**.  
Esses dados, por sua vez, serão salvos como produtos simples e poderão ser visualizados no **TOL/TRE** em: **Cadastro - Produtos Simples.**

**Tipos de Veículo**  
**Tipo de Fluxo: TOTVS OMS x TOL/TRE**.  
**Mensagem: VehicleAcquisitionService**  
Ao cadastrar um **tipo de veículo** no **Protheus**, quando a integração estiver ativa os dados serão enviados ao **TOL/TRE** por meio do método **VehicleAcquisitionService**.  
Esses dados, por sua vez, serão salvos como veículos e poderão ser visualizados no **TOL/TRE** em: **Cadastro - Veículos.  
  
Saiba mais**Mais informações poderão ser acessadas nos *link's*:[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-MP-OMS-Integra%C3%A7%C3%A3o-Protheus-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
[Logística - Linha Protheus - OMS - Como habilitar geração de arquivo de LOGs na integração do TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060684834-MP-OMS-Como-habilitar-gera%C3%A7%C3%A3o-de-arquivo-de-LOG-na-integra%C3%A7%C3%A3o-do-SIGAOMS-x-Cockpit-Log%C3%ADstico-Neolog)  
[Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na Integração TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003568682-MP-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-Integra%C3%A7%C3%A3o-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística  
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
