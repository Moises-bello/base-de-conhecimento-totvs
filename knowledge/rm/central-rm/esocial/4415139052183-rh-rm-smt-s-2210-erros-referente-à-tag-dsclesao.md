---
article_id: 4415139052183
category: eSocial
content_hash: 4e31a71630682facaa20704b42300b35f256102514bb99ac9d5a3f5410d13efb
fetched_at: '2026-06-28T22:47:39.106844+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: 'RH - RM - SMT - S-2210: Erros referente à tag ''dscLesao'''
type: support-article
updated_at: '2024-09-18T17:18:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415139052183-RH-RM-SMT-S-2210-Erros-referente-%C3%A0-tag-dscLesao
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035724577431) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**Ao gera o XML do evento S-2210 aparece as mensagens de erro abaixo, o que fazer ?   
  
*- O campo 'dscLesao' do registro 'atestado' é obrigatório e não está preenchido.*  
*- Erro na validação do campo 'dscLesao': Preencher com a descrição da natureza da lesão, conforme tabela 17.*  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Segurança e Saúde Ocupacional - Todas as versões  
  
**Solução**Siga os passos a abaixo para o ajuste do cadastro:

1. Acesse o menu CAT/Incidentes e edite o cadastro da CAT desejado.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/26462153992983)
2. Clique na aba Atestado Medico e avalie se o campo **Lesão** está preenchido. Caso não esteja. clique no botão novo e faça a inclusão selecionando um item no campo **Cód. Natureza**que pertença a tabela 17 do eSocial.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/26462153997335)
3. Ao realizar a inclusão ou ao avaliar um registro já incluído, clique sobre o nome do campo **Cód. Natureza**, ao abrir a janela de Natureza Medica, confira se o campo **Descrição Natureza e-Social** esta preenchido. O **Cód. Natureza** e a **Descrição Natureza e-Social**devem possuir o mesmo código.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/26462154001047)
4. Antes de salvar confira se a flag **'Utilizar no eSocial'** está marcada. Caso não esteja, marque a flag.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/26462184313367)
5. Ao salvar o registro irá aparece a mensagem: *Você já selecionou uma lesão para ser utilizada no e-Social. Deseja utilizar a seleção atual para o e-Social?*E clique em sim.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/26462184322327)

**Saiba mais**

Para maiores informações, acesse:

- [RH - RM - SMT - Evento S-2210 - CAT (Comunicação de Acidente de Trabalho)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028898652)

- [RH - RM - SMT - S-2210 - CAT (Ocorrência Acidente de Trabalho) não gera gatilho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402506860823)

- [RH - RM - SMT - Dúvidas frequentes: CAT (evento S-2210)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24475175102871)
