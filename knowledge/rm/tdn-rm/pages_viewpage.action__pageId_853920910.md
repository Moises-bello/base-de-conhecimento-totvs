---
content_hash: 1619bf42095e52f9a23bb858a66b8e4dac91153c0e36af292b75816bbc59c8cf
fetched_at: '2026-06-29T00:11:54.550272+00:00'
page_id: '853920910'
product: rm
source: tdn-rm
title: Leiaute S-1.2 - Nota Técnica 03/2024 e 04/2024
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=853920910
version: 26
---

false

**A partir das Versões:**

# Objetivo:

Adequamos o produto TOTVS Folha de Pagamento para atender ao leiaute S-1.2, conforme as alterações descritas nas notas técnicas do eSocial nº [03/2024](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-2-03-2024.pdf) e nº [04/2024](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-2-no-042024-revisada-28-06-2024.pdf) do eSocial.

---

11ParametrizaçãoParametrização

1) Criado o parâmetro da Nota Técnica (**S-1.2 NT 04/2023**) em Configurações | Parametrizador | Folha de Pagamento | eSocial | Configurações Gerais conforme demonstrado abaixo:

2) Após a liberação da versão será necessário executar os scripts de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

true1 Nota Técnica 03/2024  Nota Técnica 03/2024 

Ao selecionar a versão do leiaute "**S-1.2 NT 04/2023**" na aba de parametrização, o evento **"S-2221 -** **Exame Toxicológico do Motorista Profissional Empregado"** será liberado nos processos abaixo. Esse evento tem como objetivo registrar adequadamente os exames toxicológicos conforme as exigências legais. As informações geradas no XML são alimentadas no produto HCM.

* Fila de Eventos
* Fila de eventos | Processos | Excluir Evento da Fila
* Gerar XML Eventos Não Periódicos
* Integrar XML
* Integrar TAF
* Atualizar Status
* Exportar XML
* Limpar fila de eventos
* Atualizar Recibo de entrega eSocial

Para o passo a passo da geração do evento  **"S-2221 -** **Exame Toxicológico do Motorista Profissional Empregado"**  [clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=452401533)

1 Nota Técnica 04/2024  Nota Técnica 04/2024 

1) Tabela de Natureza de Rubricas

Criado a rubrica **"9253 Empréstimos eConsignado - Desconto"**. Essa rubrica foi disponibilizada em Administração de Pessoal | Cadastros | Eventos | Aba Identificação, conforme demonstrado abaixo:

**eConsignado**

* De acordo com o que publicamos em nosso [blog](https://informa.totvs.com/rh/protheus/esocial-notas-tecnicas-03-2024-e-04-2024/), o item 3.2 da Nota Técnica 04/2024 traz alterações referentes ao **eConsignado**. O objetivo do eSocial é antecipar-se a essa nova modalidade de empréstimos, preparando os leiautes para futuras regulamentações. No entanto, a regulamentação do **eConsignado** ainda não foi publicada, e o ambiente do Governo ainda não recepciona essas informações. Portanto, os produtos de folha de pagamento ainda não estão gerando tais dados.

2) Tipos de Tributação IRRF (Códigos de Incidência Tributária da Rubrica para o IRRF)

Incluído o tipo **"68-Desconto simplificado mensal (01/05/2023)"**. Esta opção foi disponibilizada em Administração de Pessoal | Cadastros | Eventos | Aba Inc. Descontos

**Desconto Simplificado Mensal**

Conforme publicado no [Perguntas e Respostas do eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes#10--remunera--o--pagamento-e-encerramento-de-eventos-peri-dicos) (item 10.39), o **Desconto Simplificado Mensal** servirá apenas para registro na folha de pagamento. Apesar do dado ser exportado para o totalizador do trabalhador (S-5002), o valor do desconto não será considerado pela DIRF.

Atualmente, nossos cálculos não incluem um evento com o valor do **Desconto Simplificado Mensal** gerado automaticamente. Esta implementação estará disponível em breve. Fiquem atentos a futuros comunicados no [RH Informa](https://informa.totvs.com/rh/), Pagina TOTVS News Folha de Pagamento e [Roadmap](https://produtos.totvs.com/) para mais informações sobre a disponibilização desta funcionalidade.

3) Tabela  de Categorias

Alterada a descrição da categoria 313, conforme abaixo:

| De | Para |
| --- | --- |
| Servidor público exercente de atividade de instrutoria, capacitação, treinamento, curso ou concurso, ou convocado para pareceres técnicos ou depoimentos | Servidor público exercente de atividade de instrutoria, curso ou concurso, convocado para pareceres técnicos, depoimentos ou aditância no exterior |

Esse ajuste encontra-se disponível em Administração de Pessoal | Funcionários | Aba Registros | Campo Código da Categoria eSocial, conforme demonstrado abaixo:

4) Evento "S-1010-Rubricas"

Incluída validação na tag "{tpRubr} - Tipo de rubrica" .  
**Validação:** Se natRubr = [9253], deve ser preenchido com[2].

5) Evento "S-1010-Rubricas"

Incluída validação na tag "{codIncFGTS} – Código de incidência da rubrica para o Fundo de Garantia do Tempo de Serviço - FGTS".  
**Validação**: Se natRubr = [9253], deve ser preenchido com[31].

**IMPORTANTE:** Caso o código da rubrica seja **"9253 Empréstimos eConsignado - Desconto"** o sistema irá gerar automaticamente o valor "31-Desconto eConsignado"  na tag <codIncFGTS>.

6) Eventos S-2200 /S-2206 / S2300 / S-2306

Alterada da descrição da tag "{tpRegPrev} - Tipo de regime previdenciário"

| De | Para |
| --- | --- |
| Regime Próprio de Previdência Social - RPPS | Regime Próprio de Previdência Social - RPPS, Regime dos Parlamentares e Sistema de Proteção dos Militares dos Estados/DF |

Adequação do produto em:

* Administração de Pessoal | Funcionários | Aba Situação | Campo Tipo de regime previdenciário (ou Sistema de proteção social dos militares)

* Administração de Pessoal | Funcionários | Aba Registro | Aba Estatutário / Mandato Efetivo | Campo Tipo de regime previdenciário (ou Sistema de proteção social dos militares)

* Administração de Pessoal | Funcionários | Anexo | Históricos | Histórico Estatutário | Campo Tipo de regime previdenciário (ou Sistema de proteção social dos militares)

7) Evento "S-2500 - Processo Trabalhista"

Alterada a condição do grupo "{ideResp} – Informações de identificação do contribuinte (responsável direto)", caso tenha havido imposição de responsabilidade indireta.

| De | Para |
| --- | --- |
| O (se infoContr/tpContr = [8]); N (nos demais casos) | O (se houver algum infoContr/tpContr = [8]); OC (se não houver nenhum infoContr/tpContr = [8] e houver algum infoContr/tpContr = [6]) |

8) Evento "S-2500 - Processo Trabalhista"

Alterada a validação da tag "{tpContr} - Tipo de contrato a que se refere o processo judicial ou ademanda submetida à CCP ou ao NINTER" do grupo "{infoContr} – Informações do contrato de trabalho."

| De | Para |
| --- | --- |
| Deve ser igual a [8] se o grupo ideResp for informado. | Deve ser igual a [6, 8] se o grupo ideResp for informado. |
