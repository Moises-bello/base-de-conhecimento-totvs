---
article_id: 13317899021847
category: GPE - eSocial - Processo Trabalhista
content_hash: 6c03560bf2f3260eb91686aa0d471dd0fcb14cfc0931be0fc1be47f1eb0edf4d
fetched_at: '2026-06-28T22:45:00.639417+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Premissas para
  geração dos eventos do eSocial para Processos Trabalhistas
type: support-article
updated_at: '2026-05-06T21:02:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13317899021847-RH-Linha-Protheus-GPE-eSocial-Processos-Trabalhistas-Premissas-para-gera%C3%A7%C3%A3o-dos-eventos-do-eSocial-para-Processos-Trabalhistas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15497242514967) Tempo aproximado para leitura: 00:05:00 min  
  
**Dúvida**  
Quais as atualizações, premissas e passo a passo para geração dos eventos do esocial de Processos Trabalhistas?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
O eSocial a cada dia absorve as obrigações Previdenciárias e Trabalhistas, e para isso, foi construído eventos específicos para essas informações de Processos Trabalhistas.  
  
**De acordo com o MOS versão S-1.2** - Devem ser prestadas nesse evento, independentemente do período abrangido pelas decisões/acordos, as informações relativas a:   
a) processos trabalhistas cujas decisões **transitaram em julgado do dia 1º de outubro de 2023 em diante**;   
b) acordos judiciais homologados a partir desta mesma data;   
c) processos com trânsito em julgado da decisão homologatória dos cálculos de liquidação a partir dessa mesma data, mesmo que o trânsito em julgado da sentença condenatória tenha ocorrido em data anterior;   
d) acordos no âmbito de CCP ou Ninter celebrados também dessa data em diante; ou e) determinações judiciais para cumprimento antecipado de decisão, ainda que parcial, proferidas a partir dessa mesma data.  
  
É importante observar que os eventos de processos trabalhistas, utilizam diversas informações de outros eventos para realizar a identificação das partes, como, por exemplo, as **informações relativas à identificação do empregador** e do **empregado** nos eventos **S-1000** – Informações do empregador, **S-2200- Cadastro Inicial** do vínculo e admissão do trabalhador entre outros eventos.  
  
Outro ponto importante, é na informação quanto o **vínculo trabalhista do empregado,** nas situações onde há o envio do evento S-2190 S-2190, S-2200 ou S-2300 no declarante, o eSocial irá validar essas informações já encaminhadas anteriormente.  
  
Uma vez que o empregado já tive informações como **admissão, demissão, dados de identificação, tipo de categoria e regime trabalhista, remuneração** anteriores, **o eSocial irá utilizar e validar essas informações** no evento S-2500 e S-2501.  
  
**Saiba mais sobre a regra** de quando enviar, o que é um processo trabalhistas, quem deve enviar os eventos, em que momento devem ser gerados e muito mais informações em nosso [**Espaço Legislação Processo Trabalhista eSocial**](https://espacolegislacao.totvs.com/esocial-processo-trabalhista/)  
  
Para o sistema as **principais premissas** são:

* Ter as atualizações recentes do GPE e TAF do *link* <https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais>
* Necessário [habilitação do **serviço REST**](https://tdn.totvs.com/display/public/framework/REST+ADVPL)
* Caso **não tenha o REST ativado,** deve **habilitar a porta multi protocolo**, pois a rotina TAFA552D foi criada em PO UI:  
  **TAF**: [Automação Fiscal - Configuração - Como ativar a porta multi protocolo no TAF - MPP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4477439959063)  
  **Middleware**: [RH - Linha Protheus - GPE - eSocial - Como ativar a porta multi protocolo utilizando Middleware](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27091607770775/preview/eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MjcwOTE2MDc3NzA3NzUsImV4cCI6MTcyOTAyODU1N30.2M9tSyTVF_gIedwaLJMrj0ea-ZAWUT9pujCrV9rIwxU)
* **Ter em mãos o Processo Trabalhista** que deve ser gerado, para que o preenchimento dos campos seja de acordo com o processo e gere corretamente o xml.
* Alteração dos **parâmetros**[MV\_TAFVLES e MV\_VLESOC para o leiaute S-1.1 ou superior](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8658568031127-RH-Linha-Protheus-GPE-eSocial-Como-se-adequar-ao-eSocial-leiaute-S-1-1)
* Incluir os menus Dados eSocial e Geração Eventos Trabalhistas: [RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Com realizar a criação dos menus TAFA552D e GPEM038](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12409243591703)

**Importante**

* Não possui integração com Folha, SST e Financeiro
* Foi disponibilizado no TAF o cadastro desses eventos também, disponível para clientes TAF FULL.
* Para clientes que utilizam **Middleware**, devem ser utilizadas as rotinas próprias para lançamento das informações (APTA100 e TAFA552D)
* Preenchimento dos campos de acordo com o [Leiaute do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/index.html#evtProcTrab), para que os eventos não sejam rejeitados.

**Passo a Passo para cadastro e geração:**

[**1º** RH - Linha Protheus - GPE - Como cadastrar um processo trabalhista (APTA100)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050723993-RH-Linha-Protheus-GPE-Como-cadastrar-um-processo-trabalhista)  
[**2º** RH - Linha Protheus - GPE - eSocial - S-2500 - Como incluir um processo trabalhista para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11991518984727)  
[**3º** RH - Linha Protheus - GPE - eSocial - S-2501 - Como incluir tributo para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12072324087575)  
[**4º** RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Como realizar a geração dos eventos S-2500, S-2501 e S-3500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12412564333719)  
  
**Assista** nossos **treinamentos** realizados pelo Suporte e pela Consultoria de Segmentos:  
[Tira Dúvidas **Suporte RH Protheus** - Tema eSocial Processos Trabalhistas](https://youtu.be/wrrD8zP_dOg)  
[**Espaço Legislação** | eSocial Layout S 1 1 e Processo Trabalhista |TOTVS RH Linha Protheus](https://www.youtube.com/watch?v=JWYVqg056NQ&list=PLXa8l0dq5zRkxpHqPKL7ZVYHt3urJ9VeM&index=11)  
  
**Atenção**, no anexo PDF (unidade 2) incluimos informações retiradas da videoaula do eSocial sobre como lançar cada tipo de contrato.   
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[Artigos RH Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971467-RH-Processos-Trabalhistas)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[*TOTVS Informa*](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**".*
