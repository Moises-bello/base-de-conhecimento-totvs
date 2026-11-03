---
content_hash: b17c834c76a44e09e9f925ec8055332d00a954928cbe87f244ea115202d2c25e
fetched_at: '2026-06-29T00:10:43.875042+00:00'
page_id: '551424026'
product: rm
source: tdn-rm
title: Instalação PEP RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=551424026
version: 25
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Pré-requisitos**
3. **Acessos externos**
4. **Passo a passo da instalação do PEP RM**
5. **Licenciamento**

sumario1. Visão Geral

## **01. VISÃO GERAL**

Instalação do PEP RM para clientes que utilizam o RM Gestão Hospitalar.

2. Pré requisitos

## **02. PRÉ REQUISITOS**

1. [Biblioteca RM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004987152-RM-Frame-Como-instalar-a-Biblioteca-RM);
2. [IIS](https://tdn.totvs.com/pages/viewpage.action?pageId=329024890);
3. RM Gestão Hospitalar instalado e funcional;
4. [Permissões de acesso configurados para prontuário eletrônico](https://tdn.totvs.com/pages/viewpage.action?pageId=551440299);
5. Os usuários que forem acessar o prontuário devem estar associados a  prestadores dentro do Gestão Hospitalar;
6. Configurar o host com [banco de dados default](https://tdn.totvs.com/display/LRM/Configurando+DefaultDB) ou [Multi Alias](https://tdn.totvs.com/pages/viewpage.action?pageId=287079669).
3. Acessos externos

## **03. ACESSOS EXTERNOS**

| Endereço | Porta | Descrição | Documentação |
| --- | --- | --- | --- |
| [integracao.evaltec.com.br](http://integracao.evaltec.com.br): | 7443 (HTTPS) | Assinatura Digital | - |
| [sandbox.api.memed.com.br](http://sandbox.api.memed.com.br): | 443 (HTTPS) | MEMED Homologação | [https://ajuda.memed.com.br/pt-BR/articles/2516816-1-iniciando-a-integracao](https://meet.google.com/linkredirect?authuser=0&dest=https%3A%2F%2Fajuda.memed.com.br%2Fpt-BR%2Farticles%2F2516816-1-iniciando-a-integracao) |
| [api.memed.com.br](http://sandbox.api.memed.com.br) | 443 (HTTPS) | MEMED Produção | - |
| [api.daily.co](https://www.google.com/url?q=http://api.daily.co&sa=D&source=hangouts&ust=1590869942823000&usg=AFQjCNHXWBad4X-KYjLJlKDnbTeGWF9mOw) | 443 (HTTPS) | Teleconsulta (caso utilizado) | [https://docs.daily.co/docs/getting-started-1](https://meet.google.com/linkredirect?authuser=0&dest=https%3A%2F%2Fdocs.daily.co%2Fdocs%2Fgetting-started-1) |

4. Passo a passo da instalação do PEP RM

## **04. PASSO A PASSO DA INSTALAÇÃO DO PEP RM**

* Na tela TOTVS RM Portal, selecione a opção de avançar

* Aparecerá uma tela de contrato de licença
* Ao ler os termos, marcar o checkbox ''aceito os termos de contrato de licença''
* Avançar

* Aparecerá a tela **pasta de destino**
* Selecionar o destino e avançar a tela
* Se o usuário preferir trocar, pode trocar.
* **OBS:** Recomendado não trocar o destino

* Ao aparecer a tela do tipo de instalação, marcar o checkbox **personalizada**e avançar para próxima tela

* Ao abrir a tela sobre a instalação personalizada é necessário selecionar os módulos desejados, no caso, PEP RM
* Avançar

* Aparecerá a tela de confirmação de instalação do programa
* Selecionar **instalar**

* Na tela seguinte, insira o local (**server and port**) do RM host do CorporeNet para poder usa-lo
* Avança

* Aparecerá a tela do Database Connection-Alias
* Escolher uma das opções que deseja utilizar e completas os campos
* Ok

* A próxima tela é referente ao processo de instalação
* Ao aparecer a mensagem, selecione **sim**

* Abrir os IIS

* Conferir no servidor se as pastas estão corretas

* Abrir a pasta que criou e criar o arquivo config.json na pasta **assets**

* Abrir rota das pastas
* Conferir se inclui a mesma informação que foi inserida em ''servidor''
* **OBS:** A porta 8051 é a porta padrão do RM para receber requisições HTTP. Para mais informações sobre a configurações de portas do Host [clique aqui.](https://tdn.totvs.com/display/LRM/Configurando+HttpPort+e+ApiPort)

* Feita a instalação com sucesso, é sé acessar o portal PEP RM e inserir o login

**IMPORTANTE**

---

No caso da utilização do módulo de Teleconsulta é **obrigatório** que o serviço do PEP RM seja configurado com SSL. No entanto, mesmo que não se utilize da Teleconsulta, recomendamos por segurança o uso desta configuração.

**Recomendações de Segurança no IIS**  
A partir da versão **12.1.2502**, recomendamos a aplicação de configurações de segurança no **IIS**. Confira no link abaixo a documentação detalhada com orientações sobre como configurar as [Recomendações de segurança PEP RM - Linha RM - TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=903613091)

5. Licenciamento

## **05. LICENCIAMENTO**

O PEP faz parte da solução RM Gestão Hospitalar e por este motivo o consumo de licença é compartilhado com o mesmo. Sendo assim num cenário onde temos três usuários acessando o módulo desktop e dois usuários acessando o PEP teremos um consumo de 5 licenças do RM Gestão Hospitalar.
