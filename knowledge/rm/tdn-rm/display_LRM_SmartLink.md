---
content_hash: 7fd31da1c34926a0607b2cf5669e85724285cd9b01b6a6404131af78463195b6
fetched_at: '2026-06-29T00:11:38.311342+00:00'
page_id: '784217718'
product: rm
source: tdn-rm
title: SmartLink
type: documentation
url: https://tdn.totvs.com/display/LRM/SmartLink
version: 15
---

2

O SmartLink é um conjunto de serviços, componentes e estratégias que é utilizada para conectar e integrar o RM aos TOTVS Apps.

Nesta página trataremos sobre a integração do SmartLink com o RM, com todos seus requisitos, processos e resolução de possíveis problemas.

A integração habilita o envio de dados do RM para o aplicativo TOTVS Apps através do **Data Sharing**, e a troca de mensagens e comandos através do **Behavior Sharing**. Estes são os mecanismos utilizados para a integração com os TOTVS Apps.

## **Requisitos da integração**

---

Para que o seu RM possa integrar com o SmartLink, é necessário que pelo menos um ambiente em que o servidor de aplicação foi implantado esteja dentro dos requisitos. Se este não for o caso, a integração não funcionará.

### Requisitos de Software

* + **Sistema Operacional:**
    - Windows Server 2019 com o build 17763.3232 ou superior;
    - Windows Server 2022;
    - Windows Server 2025;
    - Windows 11.
  + **Liberação em firewalls:**
    - Caso haja restrição de acesso a URLs, devem ser liberadas no firewall.  
      *Acessar a documentação: **[URLs utilizadas](https://tdn.totvs.com/x/8dcxPw)***.
  + **TLS 1.2** **habilitado.**

### Requisitos de Hardware

Estar dentro da portabilidade da versão respectiva do RM.  
*Acessar a documentação: **[Portabilidade - Linha RM](https://tdn.totvs.com/x/XDVNDQ)***.

## **Ativação**

---

Para ativar a integração em seu ambiente, estando ele em conformidade com os requisitos, é necessário seguir os passos abaixo.  
*Acessar a documentação: **[Ativação da integração com o SmartLink](https://tdn.totvs.com/x/feYQMg)**.*

## **Solução de conflitos**

---

Com o intuito de garantir a confidencialidade e confiabilidade da integração, o status da integração é sensível às seguintes alterações:

* + Tipo de ambiente do RM;
  + Nome e/ou servidor de banco de dados;
  + ERP associado ao ambiente.

Caso haja alteração de alguma destas informações, a **integração será removida**, e será necessário seguir os passos abaixo.  
*Acessar a documentação: **[Solução de conflitos](https://tdn.totvs.com/x/kucxPw)***.

## **Troubleshooting**

---

A ferramenta principal de diagnóstico para cenários em que seja necessário analisar o status ou qualquer tipo de informação sobre a integração é Tela de Diagnóstico.   
Para mais informações de como utilizá-la, *acessar a documentação: **[Tela de diagnóstico da integração com o SmartLink](https://tdn.totvs.com/x/YcnLPQ)***.

### Problemas em ambientes com vários servidores

Caso o ambiente possua mais de um servidor apontando para o mesmo banco de dados, as seguintes observações são válidas de atenção:

* + - Todos os servidores devem apontar para o banco de dados, em seu arquivo de gerenciamento de *alias*, utilizando o mesmo DNS e nome de servidor. Mesmo que dois nomes diferentes apontem para o mesmo servidor, isto gerará um conflito.
    - Caso algum dos servidores que possui um host ativo do RM não cumpra os requisitos de software da integração, é possível configurar uma lista dos servidores permitidos a executarem a integração.  
      Para mais informações, *acessar a documentação: **[WhiteList de servidores](https://tdn.totvs.com/x/BugxPw)***.

### Problemas com o mecanismo de envio de dados através do Upstream Data Sharing 2.0

*Acessar a documentação: **[Troubleshooting Data Sharing](https://tdn.totvs.com/x/w_oxPw)***. 

### Problemas com o mecanismo de envio ou recebimento de mensagens e comandos através do Behavior Sharing

*Acessar a documentação: **[Troubleshooting Behavior Sharing](https://tdn.totvs.com/x/1OoxPw)***.

## **Outras documentações**

---

### Detalhes sobre o funcionamento

Para mais informações sobre o funcionamento da integração com o Data Sharing Upstream 2.0, acesse o documento: [Integração RM x SmartLink Data Sharing 2.0](https://tdn.totvs.com/x/CqviM)

Já para o Behavior Sharing, o documento pode ser acessado: [Integração RM x SmartLink Behavior Sharing](https://tdn.totvs.com/x/5gEGJw)

### Integração com o TOTVS Apps

Para informações sobre a integração legado com o SmartLink Data Sharing 1.0, acesse a documentação: [Integração RM x SmartLink Data Sharing 1.0](https://tdn.totvs.com/x/l-55IQ)

## **Novidades e Melhorias**

---

### O que mudou nessa versão

A partir da versão 12.1.2606, 12.1.2602 patch 172 e 12.1.2510 patch 258

* + Serviço de carga inicial passa a ser realizado de forma automática quando identificado que existem tabelas ainda não integradas, ou seja, que nunca houve pelo menos 1 Force Reload concluído.  
    Quando uma nova tabela for adicionada no aplicativo do produto, a integração e envio de dados desta tabela passa a ser realizada de forma automática não havendo mais necessidade de solicitar sinalização de Force Reload.
  + As colunas RecModifiedOn e RecCreatedOn passam a ser colunas com dados obrigatórios para controle do Force Reload e principalmente do Delta.   
    Caso seus valores estejam nulos, o envio deste registro será ignorado.   
    O Delta será sempre realizado baseado na informação de Data e Hora da coluna RecModifiedOn mais atual, entendendo que houve alteração em algum dado do registro.
  + O serviço de Force Reload ocorre a cada 2 minutos e o Delta a cada 15 segundos.   
    Estes intervalos podem sofrer ocasionalmente um atraso, a execução não se sobrepõe ou acumula, dessa forma, caso um Delta demore por exemplo 45 segundos, a próxima execução será 15 segundos após a conclusão do anterior.
  + O Force Reload passa a filtrar os dados com D-1 para evitar perda de dados que estiveram em transações longas.   
    Assim, o primeiro Delta subsequente ao FR vai realizar o envio do dia faltante e equalizar o sincronismo de dados atualizados enviados.  
    Do segundo Delta em diante começam a serem enviados os registros com o RecModifiedOn mais atual.
  + O envio de dados da Carga Inicial e do Force Reload não grava mais nenhum dado na tabela GDATASHARERECORDS, apenas o Delta continua gravando dados para que sirva de controle de atualizações.  
    Dessa forma essa tabela terá redução significativa de volume de dados.  
    Seus dados serão mantidos por até 3 dias e possui um serviço de sanitização diária.
  + Melhoria e evolução na tela de Diagnóstico, trazendo melhor visualização e experiência ao usuário para auxiliar na identificação de problemas.
  + Alteração no modo de identificação do ambiente RM com o SmartLink.  
    Esta melhoria poderá necessitar de uma reconfiguração das credenciais em ambientes que já se encontram integrados.  
    Para tanto, em caso desta necessidade, utilize o assistente de ativação,

#0c9abesolid

ÚLTIMAS ATUALIZAÇÕES

page10socialsmart-link-rm
