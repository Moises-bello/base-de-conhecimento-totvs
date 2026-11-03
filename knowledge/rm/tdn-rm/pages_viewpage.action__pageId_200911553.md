---
content_hash: f17b276661bbe1e6ae88e3144c2de629819fad4eb2e8b4db6457850f0ea80390
fetched_at: '2026-06-29T00:06:04.809468+00:00'
page_id: '200911553'
product: rm
source: tdn-rm
title: Balanceamento nativo (Múltiplos Hots)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=200911553
version: 9
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Performance                        **Versão:**11.82.39 |
| **Processo** | **:** | Balanceamento de Conexões x Servidor de Aplicação |
| **Subprocesso** | **:** | Configurações de Balanceamento - Dimensionamento de requisições |
| **Data da publicação** | **:** | 01/09/2015 |

Com o Balanceamento Nativo, todas as requisições serão balanceadas entre os hosts disponíveis descritos no arquivo de configuração do aplicativo (**RM.exe.config** ou outros como por exemplo **RMLabore.exe.config**), mantendo o consumo de memoria RAM e CPU dimensionado entre eles (4 serviços RM.Host.Service). Além disso, quando se utiliza Multiplos Hots é possível obter contingência caso algum deles venha a ter inconsistência, não afetando o ambiente de produção.

Desmarque a função "Somente leitura" da pasta ..\RM.Net (**C:\TOTVS\CorporeRM\RM.Net**)

Execute o aplicativo **RM.Host.ServiceManager.exe**, disponível em **C:\totvs\CorporeRM\RM.Net**

Altere a quantidade de serviços para 4 (a recomendação é para cada Host, 25 usuários).

Clique em **Instalar**, para cada novo serviço.

No Gerenciador de Tarefas, irá ficar como abaixo:

Abra os arquivos de configuração (\*.config) de cada aplicativo e altere a porta de comunicação seguindo a mesma sequencia definida no passo anterior (8050, 8052,8054, 8056).

Após, a configuração o arquivo deverá ficar como o exemplo a baixo. Essa mesma configuração deve ser feita para os aplicativos (RMLabore.exe.config, RMChronus.exe.config etc).

Neste arquivo, recomendamos a utilização do IP no local de hostname evitando passar no DNS.

No caso do portal, a configuração deverá ser realizada no arquivo **Web.config** disponível em **C:\totvs\CorporeRM\Corpore.Net.** Neste caso deve reiniciar o IIS.

**Lembrando que as portas de comunicação devem estar liberadas em REDE.**

---

Além disso, recomendamos a habilitação da função de execução dos programas como Administrador para todos os usuários.

Para habilitar, acesse as propriedades dos programas abaixo, posteriormente habilite o parâmetro informado na caixa de “Nível de privilégio”.

* RM.Host.exe
* RM.Host.Service.exe (Inclusive para servidores que obter múltiplos hots, em todos os serviços)
* RM.Host.JobRunner.exe
* RM.Lib.Gerador.Execute.exe

Para que os serviços iniciem quando o servidor for reiniciado ou tiver algum erro, realize as configurações abaixo:

**RM.Host.Service**

**RM.Host.Service1**

****RM.Host.Service2****

******RM.Host.Service3******
