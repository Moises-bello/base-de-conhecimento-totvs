---
content_hash: 532d5af56b7adcd39baef94e3c93fb5fe017c68f3078f92a6baeed92b653f14e
fetched_at: '2026-06-29T00:09:16.131376+00:00'
page_id: '421385462'
product: rm
source: tdn-rm
title: Integração com ORCECERTO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385462
version: 2
---

---

A ORCECERTO é uma empresa que realiza soluções de informação, conhecimento e sistemas de apoio à indústria da construção. Ela possui uma base de dados que contém uma grande e atualizada lista de composições, insumos e preços. No TOTVS Obras e Projetos existe a Integração com a base PINI que será substituída pela integração com a ORCECERTO.

A integração do TOP com a ORCECERTO se dá através do consumo dos serviços do WebService que alimentam a base do TOP. O WebService contará com nove serviços a serem consumidos pela TOTVS em seu processo de importação:

**Cadastrar Senha:**

Este serviço irá cadastrar a senha do cliente TOTVS no WebService do sistema ORCECERTO. O TOTVS irá enviar um arquivo XML contendo um cabeçalho com o "código de usuário" para autenticar o serviço, o CNPJ do cliente TOTVS, e a senha que o cliente informou nos parâmetros do TOP.

**Alterar Senha:**

Este serviço irá alterar a senha do cliente TOTVS no sistema. O TOTVS irá enviar um arquivo XML contendo um cabeçalho com Usuário e Senha para autenticar o serviço e no corpo terá a nova Senha que o cliente informou nos parâmetros.

**Obter Versão:**

Este serviço irá retornar a versão da base padrão ORCECERTO disponível, e a referência de preços atual. O TOTVS irá enviar um arquivo XML contendo um cabeçalho com Usuário e Senha para autenticar o serviço, e no corpo enviará a versão da base padrão ORCECERTO assim como o ano e mês da referência de preços ORCECERTO que está atualmente no cliente TOTVS.

**Obter Praças:**

Este serviço irá retornar todas as praças de preços disponíveis para esse cliente TOTVS. O TOTVS irá enviar um arquivo XML contendo um cabeçalho com Usuário e Senha para autenticar o serviço.

**Obter Naturezas Insumos:**

Este serviço irá retornar todas as naturezas dos insumos disponíveis no WebService. O TOTVS irá enviar um arquivo XML contendo um cabeçalho com Usuário e Senha para autenticar o serviço. As naturezas de insumos ORCECERTO equivalem aos "Grupos de Custo" no TOP.

**Obter Insumos:**

Este serviço irá retornar todos os insumos da base de dados padrão ORCECERTO no WebService. O TOTVS irá enviar um arquivo XML contendo um cabeçalho com Usuário e Senha para autenticar o serviço e no corpo a versão de base padrão ORCECERTO atual do cliente.

**Obter Preços Insumos:**

Este serviço é um dos mais importantes no processo e irá retornar todos os preços de insumos da praça escolhida pelo cliente no processo de Importar base. O TOTVS irá enviar um arquivo XML contendo um cabeçalho com Usuário e Senha para autenticar o serviço e no corpo terá a praça e o ano e mês da referência de preços atual do cliente TOTVS. Os preços serão importados em moeda brasileira (Real – R$), pois as praças que ao WebService trabalha são todas do território nacional.

**Obter Composições:**

Este serviço irá retornar todas as composições da base de dados dao WebService. O TOTVS irá enviar um arquivo XML contendo um cabeçalho com Usuário e Senha para autenticar o serviço e no corpo a versão da base padrão ORCECERTO atual no cliente.

**Obter Recursos Composições:**

Este serviço irá retornar todos os recursos de composições da base ORCECERTO. O TOTVS irá enviar um arquivo XML contendo um cabeçalho com Usuário e Senha para autenticar o serviço e no corpo a versão da base padrão ORCECERTO atual do cliente.

Para clientes que utilizam a integração com a PINI, existe a opção, no sistema de realizar a conversão para a integração com a ORCECERTO, essa opção está presente na tela de Parâmetros Gerais do TOP e após executar a conversão da integração os campos de Url, Login e Senha deverão ser informados. Após a conversão todas as descrições que anteriormente faziam referência à PINI passam a se referir à ORCECERTO.

---
