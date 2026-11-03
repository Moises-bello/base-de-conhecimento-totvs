---
content_hash: 367d0dc10f6cc23059a3a184100388136fa01ab86b1385ac0f910dc759f76f37
fetched_at: '2026-06-29T00:11:22.155278+00:00'
page_id: '699816440'
product: rm
source: tdn-rm
title: Relatório do Espelho do Ponto Eletrônico - Portaria 671/2021
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=699816440
version: 33
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: |  |
| Segmento: | RH |
| Módulo: | Relatórios - Portaria 671 |
| Função: | Permitir  a emissão do Relatório atendendo a Portaria 671 |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHJORNRM-2371](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-2371)  [DRHJORNRM-2416](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-2416)  [DRHJORNRM-2372](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-2372)  [DRHJORNRM-2374](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-2374) |

## **02. SITUAÇÃO/REQUISITO**

Permitir a geração do relatório do espelho do ponto eletrônico da Portaria 671/2021

## **03. SOLUÇÃO**

Criado menu que permite gerar o relatório do espelho do ponto eletrônico da Portaria  671/2021

## **04. EXEMPLO DE UTILIZAÇÃO**

11Parametrização

É necessário importar a estrutura do relatório **PTOREL01.0011.**

**Observação:** Para as versões até a 12.1.34 importe o relatório conforme o artigo [Como importar estrutura de relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022591971-TOTVS-RH-Linha-RM-PTO-Como-importar-estrutura-de-relat%C3%B3rios). Em versões superiores importe conforme o artigo [TOTVS Compartilhamento](https://tdn.totvs.com/display/public/LRM/TOTVS+Compartilhamento#TOTVSCompartilhamento-DownloaddeobjetogerencialnoTOTVSCompartilhamento).

Verifique se o tipo do relatório importado está definido como **Portaria 671/2021**.

Para acessar o relatório espelho da Portaria 671/2021o usuário deve ter a permissão no perfil. Para conceder a permissão acesse **Serviços Globais | Segurança | Perfis | Selecione o sistema Automação de Ponto | Selecione o usuário desejado | Editar | Acesso a Menus | [06.05] Portaria 671/2021 | [06.05.02] Espelho | Permitir acesso | OK**.

Para que a **Duração da Jornada realizada**seja exibida, é necessário que os funcionários estejam com o parâmetro **Pagar Horas Trabalhadas** marcado. Se o parâmetro não estiver marcado a coluna será exibida sem valor.  
Para verificar o parâmetro acesse **Cadastros | Funcionários | Selecione o funcionário desejado | Processos | Parametrizar Funcionário | Etapa 11 - Horas Trabalhadas | Pagar Horas Trabalhadas**.

2Relatório do Espelho do Ponto Eletrônico da Portaria - 671/2021

Para gerar o relatório Espelho da Portaria 671/2021 acesse **Relatórios | Portaria 671/2021 | Espelho**.

Informe os parâmetros e clique em Executar.

O Relatório será exibido conforme os seguintes exemplos:

**Exemplo horário diurno**

**Exemplo horário noturno**

**Observações:**

* A segunda coluna que representa a **Duração da Jornada Realizada** é calculada por dia, então deve ser analisada dia a dia.
* Em horários noturnos os dias se repetem no relatório, pois uma jornada termina e uma nova se inicia no mesmo dia. Nesse caso a **Duração da Jornada Realizada** do dia também será exibida mais de uma vez.

**04. ASSUNTOS RELACIONADOS**

**[Parâmetros do Relatório Espelho do Ponto Eletrônico - Portaria 671/2021](https://tdn.totvs.com/pages/viewpage.action?pageId=699816678)**
