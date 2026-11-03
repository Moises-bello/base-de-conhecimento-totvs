---
content_hash: a393bf1a42d3886cd744c11dfea617d9bd54d46bbdb199bed787c54afe79a2af
fetched_at: '2026-06-29T00:08:19.306013+00:00'
page_id: '267780365'
product: rm
source: tdn-rm
title: Parametrizações para iniciar o Rm.Host.Service
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267780365
version: 6
---

# Configurações para iniciar o host

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.XX; 12.1.XX |
| **Ocorrência:** | Configurações para o host quando se tem alguma inconsistência no processo de inicialização |
| **Ambiente:** | Ambiente de Instalação/ Teste/ Produção |
| **Passo a passo:** | Desinstalar o serviço do HOST, apagar o arquivo (\_Broker.dat) alterar a conta para LOCAL SISTEM, após isso instalar novamente. Para localizar o arquivo acesse : C:\totvs\CorporeRM\RM.Net             **INICIALIZAÇÃO DO HOST** Para verificar essa opção acesse os serviços do Windows.          **RECUPERAÇÃO DO HOST**      **Usuário Host**  Dessa forma, mesmo que o usuário não seja administrador da máquina, o serviço do RmHost sera iniciado como administrador do Sistema. |
| **Observações:** |  |
