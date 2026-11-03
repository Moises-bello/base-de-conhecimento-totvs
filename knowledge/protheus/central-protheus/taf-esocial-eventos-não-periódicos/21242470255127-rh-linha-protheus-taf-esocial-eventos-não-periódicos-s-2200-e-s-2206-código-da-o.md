---
article_id: 21242470255127
category: TAF - eSocial - Eventos Não Periódicos
content_hash: d64bcefbcaedc285478e9a18c91196ec3efe3e8002f7cf5d97925aff4cde41c8
fetched_at: '2026-06-28T22:45:18.013203+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Não Periódicos - S-2200 e S-2206
  - Código da Ocorrência: 8 - Grupo ''Informacoes relacionadas ao aprendiz'' deve
  ser preenchido. Verifique as condicoes de preenchimento no leiaute.'
type: support-article
updated_at: '2024-08-27T19:26:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21242470255127-RH-Linha-Protheus-TAF-eSocial-Eventos-N%C3%A3o-Peri%C3%B3dicos-S-2200-e-S-2206-C%C3%B3digo-da-Ocorr%C3%AAncia-8-Grupo-Informacoes-relacionadas-ao-aprendiz-deve-ser-preenchido-Verifique-as-condicoes-de-preenchimento-no-leiaute
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21242470219671) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Ao tentar transmitir o evento periódico S-2200 (Cadastro Inicial de Vínculo e Admissão) ou o evento S-2206 (Alteração de Contrato de Trabalho), o governo (eSocial) retorna com a seguinte inconsistência:  
  
**Sequência: 000001 - Tipo: Erro - Codigo da ocorrência: 8****Localização: /eSocial/evtAltContratual/altContratual/vinculo/infoRegimeTrab/infoCeletista****Descrição: Grupo 'Informacoes relacionadas ao aprendiz' deve ser preenchido. Verifique as condicoes de preenchimento no leiaute.****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - TAF - eSocial - Todas as versões  
  
**Causa**O erro ocorre devido a falta de preenchimento de campos obrigatório, conforme o Leiaute S-1.2, nos eventos S-2200 ou S-2206, referentes ao Menor Aprendiz.   
 **Solução****1.** Certifique-se que o ambiente está atualizado com a última **Expedição Contínua do TAF**, assim como o dicionário que deve também estar atualizado (para o dicionário ser atualizado, é necessário rodar o **UPDDISTR**).

12.1.33 - Para segregados e para clientes Protheus que possuem Garantia Estendida:  
<https://suporte.totvs.com/portal/p/10098/download?e=1043538>  
12.1.2210 - Para segregados e para clientes Protheus que possuem Garantia Estendida:  
<https://suporte.totvs.com/portal/p/10098/download?e=1084563>  
12.1.2310:  
<https://suporte.totvs.com/portal/p/10098/download?e=1126399>

**Para mais detalhes referente a atualização do TAF, verifique a documentação abaixo:**  
[Automação Fiscal - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239)  
  
**2.** No TAF, para preenchimento dos campos, acesse o evento S-2200 ou S-2206 (Atualizações > Eventos eSocial > Trabalhador > Cadastro Trabalhador) e selecione o botão **Alterar**:  
[RH - Linha Protheus - TAF - eSocial - Eventos Não Periódicos - S-2200/S-2300 - Como acessar a rotina de cadastro do trabalhador no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036524534):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21242486075287)  
  
Na aba **Vínculo - Informações do Contrato** e no subgrupo **Informações do Empregador** **Contratante de Aprendiz**, onde poderá preencher os campos, conforme manual do eSocial:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21242486081559)  
![chrome_dpP9PGLEGj.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25946849782935)  
  
⚠️ Para preenchimento dos respectivos campos no ERP de origem, Protheus Recursos Humanos, RM Labore, Datasul ou demais ERP´S, é necessário acionar a equipe correspondente, através de abertura de chamado ou chat da TOTVS.

**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
