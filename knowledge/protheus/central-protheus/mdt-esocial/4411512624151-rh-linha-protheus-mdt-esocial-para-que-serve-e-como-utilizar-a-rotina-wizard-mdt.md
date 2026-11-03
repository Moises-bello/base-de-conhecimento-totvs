---
article_id: 4411512624151
category: MDT - eSocial
content_hash: 5ed613af7616c6f104007b34f114052a3a3dd1dd185408f92ebf768ddf815a76
fetched_at: '2026-06-28T22:44:29.265304+00:00'
product: protheus
section_id: 360004428991
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - Para que serve e como utilizar a rotina
  Wizard MDT (MDTA891) no eSocial
type: support-article
updated_at: '2025-08-04T12:59:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411512624151-RH-Linha-Protheus-MDT-eSocial-Para-que-serve-e-como-utilizar-a-rotina-Wizard-MDT-MDTA891-no-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25308146341911) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Para que serve e como utilizar a rotina **Wizard MDT** (MDTA891) no eSocial?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**  
A rotina **Wizard MDT** (MDTA891) tem como objetivo **importar** a descrição e códigos de tabelas oficias do **eSocial** para dentro do modulo Medicina e Segurança do Trabalho (SIGAMDT). Ao executar esse **Wizard** o sistema cria registros nas tabelas (rotinas) abaixo com a descrição e código eSocial.  
  
A importação ocorre para as seguintes rotinas:

* [Tabela 13 - Parte do corpo atingida](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.3/tabelas.html#13): Localizada no menu: atualizações > acidente de trabalho > Parte do Corpo Atingida (MDTA603);
* [Tabela 14 - Agente Causador do Acidente de Trabalho](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.3/tabelas.html#14): Localizada no menu: atualizações > acidente de trabalho > Obj.Causador Acid. (MDTA605);
* [Tabela 15 - Agente Causador / Situação Geradora de Doença Profissional ou do Acidente de Trabalho](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.3/tabelas.html#15): Localizada no menu: atualizações > acidente de trabalho > Tipos de Acidentes (MDTA600);
* [Tabela 17 - Descrição da Natureza da Lesão](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.3/tabelas.html#17): Localizada no menu: atualizações > acidente de trabalho > Natureza da Lesão (MDTA604);
* [Tabela 24 - Agentes Nocivos e Atividades - Aposentadoria Especial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.3/tabelas.html#24): Localizada no menu: atualizações > PPRA > Agentes (MDTA182);

**Observação**  
A **Wizard de Importação** está localizada no modulo SIGAMDT no caminho: Miscelânea - Implantação - **Wizard MDT**(MDTA891). É necessario seguir os procedimentos da documentação: **[Wizard de Importacao eSocial](https://tdn.totvs.com/x/NITpEg)** para efetuar a configuração.  
  
**Importante**

* A execução dessa rotina não é obrigatória, ela é apenas um facilitador para criar registros automáticos;
* Ao executar a rotina o sistema cria registros nas tabelas de acordo com a descrição e código **eSocial**, esses códigos ficam apenas no **SIGAMDT** e não devem ser confundidos com os códigos do **SIGATAF**;
* Ao executar a rotina, o sistema cria todos os registros conforme as tabelas. Portanto, execute-a apenas se desejar que o sistema gere todos os códigos automaticamente. Caso contrário, os registros podem ser cadastrados individualmente, acessando as rotinas mencionadas acima.

Veja também o vídeo de exemplo sobre essa rotina:  
How To | SIGAMDT eSocial SST - Wizard Importação de Tabelas eSocial  
  
 **Saiba Mais**  
[Qual a funcionalidade da rotina Conciliação eSocial (MDTA890)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033129413)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
