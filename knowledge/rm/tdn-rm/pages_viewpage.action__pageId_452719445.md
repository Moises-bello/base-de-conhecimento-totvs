---
content_hash: 0f1ccb9dd1caf19ca6d5872845472ac9057d92de212f94041f0b6e7c3247d533
fetched_at: '2026-06-29T00:10:07.817142+00:00'
page_id: '452719445'
product: rm
source: tdn-rm
title: Integração com o TAF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719445
version: 22
---

1true1Aba Integração com TAFAba Integração com TAF

Nesta etapa, você deverá realizar a parametrização completa da configuração necessária para estabelecer uma conexão com o TAF, permitindo assim a transmissão dos eventos do eSocial.  
   
**URL WebService**  
Informe o dados do webservice que será usado para transmitir as informações ao TAF.

* **Servidor:** Nome do servidor
* **Porta:** Número da porta

**Usuário**  
Usuário para autenticação no TAF.  
   
**Senha**  
Senha para autenticação no TAF.  
   
**Código da Filial TAF**  
Informar o código da filial que será considerada no TAF para recebimento das informações transmitidas.

**Observação**: Deve ser parametrizado de acordo com o que está preenchido no campo "Cód Filial" presente no cadastro de Complemento Cadastral - TAF.

**Utilizar relacionamento Filial RM x Filial TAF para eventos de funcionário**  
Com esse parâmetro será possível fazer com que o RM transmita os eventos de funcionário (não entra autônomos externos e autônomos do sistema TOTVS Gestão Financeira) para sua filial correspondente no TAF.

**PONTOS DE ATENÇÃO AO MARCAR O PARÂMETRO**

1. Passa a ser necessário configurar todas as filiais (que possuem eventos de funcionário) na etapa Filiais (RM x TAF) .
2. Os eventos de tabela serão enviados para a filial que se encontra configurada no campo "Código da Filial TAF".
3. As tabelas de negócio do TAF relacionadas ao Eventos de Tabela do eSocial devem, obrigatoriamente, estar compartilhadas. A realização do compartilhamento de tabelas, por sua vez, só é indicado no momento da implantação do TAF.
4. Nos casos de autônomos externos, autônomos do TOTVS Gestão Financeira e funcionários com cadastro de múltiplos vínculos, os eventos serão integrados na matriz do TAF.
5. Serão considerado os eventos:S-1200, S-1202, S-1207, S-1210, S-2200, S-2205, S-2206, S-2210, S-2220, S-2230, S-2231, S-2240, S-2298, S-2299, S-2300, S-2306, S-2399, S-2400, S-2405, S-2410, S-2416, S-2418, S-2420 e S-3000.
6. Para os eventos periódicos: S-1200, S-1202, S-1207, S-1210 e S-3000 de periódicos, quando a geração for para competências retroativa a atual, sempre será verificado o histórico de seção.

**Exemplo:**

Na competência atual (11/2022) é enviado uma retificação do evento S-1210 referente a competência 10/2022, o sistema irá enviar o evento para filial cadastrada no histórico de seção do mês 10/2022.

**Utilizar filial padrão**  
A utilização desse parâmetro fará com que todos os eventos de funcionário que tenham por origem uma filial que não esteja configurada na etapa Filiais (RM x TAF), seja transmitido para uma filial padrão do TAF.  
   
**Utilizar fila de integração**  
Ao marcar esse parâmetro, os eventos enviados para o TAF serão adicionados na "fila de integração" caso exista algum evento predecessor não integrado.

**Observação:** Para mais detalhes sobre a fila de integração no TAF clique veja: [Manual de Integração - TAF - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=274304871)

true2Aba Outros ParâmetrosAba Outros Parâmetros

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
