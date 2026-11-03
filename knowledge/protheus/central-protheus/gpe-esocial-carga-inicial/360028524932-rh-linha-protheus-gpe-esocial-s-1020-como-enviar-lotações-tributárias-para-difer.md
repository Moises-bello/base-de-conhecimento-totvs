---
article_id: 360028524932
category: GPE - eSocial - Carga Inicial
content_hash: a14c5576d9163595527890596d5d843c1cb76437de2b9e42964471bffa4fdfec
fetched_at: '2026-06-28T22:45:03.314841+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1020 - Como enviar Lotações Tributárias
  para diferentes filiais quando há diferentes códigos de FPAS e Terceiros
type: support-article
updated_at: '2026-04-06T18:01:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028524932-RH-Linha-Protheus-GPE-eSocial-S-1020-Como-enviar-Lota%C3%A7%C3%B5es-Tribut%C3%A1rias-para-diferentes-filiais-quando-h%C3%A1-diferentes-c%C3%B3digos-de-FPAS-e-Terceiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28117261230359) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
S-1020 - Como enviar Lotações Tributárias para diferentes filiais quando há diferentes códigos de FPAS e Terceiros?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Para existir uma lotação tributária com o FPAS e/ou código de terceiros de acordo com cada Filial o cadastro de Centro de Custo e tabelas relacionadas deverão ser exclusivas por Filial.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029480292)  
  
Segue abaixo a documentação com a relação das tabelas do GPE x TAF, lembrando que deve alterar sempre via configurador para também alterar as tabelas filhas.  
[**Como deve ser definido o Compartilhamento de Tabelas SIGAGPE x SIGATAF**](http://tdn.totvs.com/display/PROT/Como+deve+ser+definido+o+Compartilhamento+de+Tabelas+SIGAGPE+x+SIGATAF)  
  
Para o eSocial a alíquota de INSS - **Outras Entidades** é calculada com base no **FPAS** e código de terceiros e não com a alíquota informada na tabela S038 do GPE.  
Exemplo [**tabela 04**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s-1-3-cons-nt-05-2025/tabelas.html#04):   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39551789086231)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39551777575703)​  
  
O código de lotação do evento **S-1020** é composto pelo código do Centro de Custo e quando é exclusivo ele também é preenchido com o código da Filial de acordo com o seu **SIGAMAT**.  
  
![](https://totvssuporte.zendesk.com/attachments/token/MprkmjtpRiL8S61c1I20XYG5n/?name=inline-417321008.png)​  
  
Se o modo de acesso for compartilhado o **Sistema** só gravará o Código do Centro de Custo e o Governo não aceita o mesmo código de Lotação duas vezes para a mesma raiz de CNPJ, ou seja, o Protheus realizará o envio ao TAF somente da Matriz.  
Recentemente foi criado um novo controle de lotações tributária do eSocial que não são vinculadas ao Centro de Custo, mas isso é novo e não existia nas tratativas anteriores e não pode ser confundida com as orientações já passadas, caso tenha interesse em utilizado sugiro que leia completamente a documentação "[RH - Novo Controle de Lotações](http://tdn.totvs.com/x/PCcxHQ)" e realize as parametrizações informadas.  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[Artigos S-1020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051258534)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Para conhecimento dos **eventos futuros**, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
