---
content_hash: 13d86a419059d018adb0f6e8cfeed453b2b10b042acf63829514ccea356f8452
fetched_at: '2026-06-29T00:10:51.349735+00:00'
page_id: '566479573'
product: rm
source: tdn-rm
title: Integração com Middleware
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=566479573
version: 10
---

Após a ativação do Middleware, a configuração correspondente estará acessível nesta etapa do parametrizador.

1true1Aba IntegraçãoAba Integração

**Web Service**  
Informe o dados do webservice que será usado para transmitir as informações ao TAF.

* **Servidor:** Nome do onde o middleware está instalado
* **Porta:** Número da porta de conexão com o servidor que possui o middleware instalado
* **Usuário:**Usuário para autenticação no TAF.
* **Senha:** Senha para autenticação no TAF.

**Web Service TSS**

* URL WebService TSS.

Para mais detalhes, acesse: [Como realizar a configuração da URL do TSS e onde informar o Certificado Digital para realizar a transmissão dos eventos do eSocial para o governo?](https://tdn.totvs.com/pages/viewpage.action?pageId=334334296)

2Aba Certificado DigitalAba Certificado Digital

Dados do Certificado digital

**Tipo de Certificado Digital:**Este campo permite selecionar qual tipo de certificado será utilizado para envio das informações ao eSocial.

* **A1-Formato PFX (.pfx ou .p12)**

Clique no lookup e selecione o [certificado digital](https://tdn.totvs.com/display/LRM/Middleware+-+Certificado+Digital) desejado.

* **A3- HSM (Hardware Security Module)**

**slot:** Número do Slot

**idHex:** Id Hexadecimal. Esta informação pode ser substituída pelo campo module.

**Localização do Module:**Caminho da DLL da máquina onde o certificado encontra-se instalado. Esta informação pode ser substituída pelo campo idHex. (obs: se informado, o TSS deve ter acesso ao diretório)

**label:** Label do certificado digital

**Atualizar Certificado TSS:** Ao clicar neste parâmetro o irá realizar a validação dos dados cadastrados nesta aba e irá atualizar o certificado configurado.

true3Aba Outros ParâmetrosAba Outros Parâmetros

Dados Complementares

**Identificador da tabela de rubricas utilizadas pelo TAF:** Caso já tenha enviado rubricas através do TAF OnPremisse, deverá informar nesse campo o Identificador de Tabela de Rubricas gerado pelo TAF.

**Desativar predecessão de envio de eventos:**Caso esse parâmetro for marcado, o sistema não validará a ordem de envio de eventos ao eSocial. Essa ordem de envio é determinada pelo MOS(Manual de Orientação do Esocial) vigente. Se desmarcado, serão feitas as seguintes validações:

* Ao enviar eventos de tabela: Para todos os eventos de tabelas com operação de Alteração, será verificado se existe na fila um evento pendente\* de Inclusão ou Carga Inicial do mesmo. Se existir o evento pendente, o processo será finalizado com erro.
* Ao enviar os eventos Periódicos e Não periódicos: Para os eventos periódicos (S-1200, S-1202 e S-1210) e para os eventos não periódicos (S-2205, S-2206, S-2210, S-2220, S-2221, S-2230, S-2240, S-2245, S-2250, S-2260, S-2298, S-2299, S-2306, S-2399), será verificado se existe na fila um evento pendente\* do tipo S-2200 ou S-2300 com operação Inclusão ou Carga Inicial para o funcionário. Se existir o evento pendente, o processo será finalizado com erro.
* Ao enviar o evento de Exclusão(S-3000): Será validado se o evento que está sendo excluído está com o status 10 - Aceito RET. Se existir o evento pendente, o processo será finalizado com erro.
* Para todos os eventos, será verificado se existe um evento S-1000 pendente na fila. Se existir o evento pendente, o processo será finalizado com erro.

\*Status considerados com Pendente: 0 - Pendente, 1- Gerado, 2- Erro na Geração, 5 - Erro de Integração e 9 - Rejeitado RET.

**Relatório de Conferência**

**Servidor/Porta API**: Servidor e porta onde o serviço de API"s RM está sendo executado. (**APiPort** do Host RM. No caso onde a ApiPort não foi discriminada nas configurações do Host, utilizar a HttpPort). 

**Servidor/Porta APP:** Servidor e porta onde o aplicativo THF está sendo executado. (Caso o servidor seja o Host RM, informar a **HttpPort**).

Para maiores informações sobre a configuração da **HttpPort** e **ApiPort**, acesse: [O que é e como configurar a HttpPort e ApiPort](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633-RM-Integra%C3%A7%C3%B5es-O-que-%C3%A9-e-como-configurar-a-HttpPort-e-ApiPort-).

**Observação:** **Se estiver executando o RM.Host.exe o mesmo deve ser executado com administrador.**

|  |  |
| --- | --- |
|  | Informações Complementares |

---

eSocial

[Parametrizador](http://tdn.totvs.com.br/display/LRM/Parametrizador)
