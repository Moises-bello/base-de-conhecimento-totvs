---
article_id: 360045713293
category: Recrutamento e Seleção de Pessoas (SIGARSP)
content_hash: 7455fa868761af915ba1b44bb176e22e153f3dc567913acb6a8af00feffe6f1d
fetched_at: '2026-06-28T22:43:00.888424+00:00'
product: protheus
section_id: 206960907
source: central-protheus
title: RH - Linha Protheus - RSP - Admissão de um candidato apresenta a mensagem "RSPDEPA.TXT"
  não foi encontrado
type: support-article
updated_at: '2022-08-29T11:17:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045713293-RH-Linha-Protheus-RSP-Admiss%C3%A3o-de-um-candidato-apresenta-a-mensagem-RSPDEPA-TXT-n%C3%A3o-foi-encontrado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:05:00 min  
  
Dúvida**No módulo 20 - Recrutamento e Seleção de Pessoal, ao realizar uma admissão, apresenta a mensagem, "RSPDEPA.TXT" não foi encontrado.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8454070039063/mceclip0.png)  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Recrutamento e Seleção de Pessoal  – Todas as versões **Solução**Esta situação ocorre quando o sistema não localiza o arquivo necessário para copiar os campos do cadastro do currículo para o cadastro do funcionário.  
A rotina de **Admissão** que fica no módulo **20 - Recrutamento e Seleção de Pessoal (SIGARSP)** no caminho **Miscelânea - Admissão (RSPM001)**,permite efetivar a Admissão de um candidato, onde os dados de seu currículo serão disponibilizados no **Cadastro de Funcionários**, facilitando o preenchimento das informações do novo funcionário.   
A rotina faz uso de um **arquivo de texto** que segue na sua estrutura os campos do **currículo (SQG)**, que serão utilizados para migrar as informações do candidato para o cadastro de funcionários (SRA), facilitando o preenchimento de parte dos campos e que por sua vez permite ao cliente fazer manutenção inserindo mais campos conforme sua necessidade.   
No configurador  **SIGACFG**, acesse o caminho: **Ambiente - Cadastros - Parâmetros**,  localize o parâmetro **MV\_RSPDEPA** que deve ser configurado com o nome do arquivo de texto, isto é, **RSPDEPA.TXT**, arquivo para a conversão dos dados do candidato para o funcionário que deverá estar na pasta **“\system”**, conforme instalação do Protheus.  
  
Segue uma breve demonstração do processo:  
  
![RSDEPA.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/8455188639767/RSDEPA.gif)  
  
Ao finalizar o preenchimento das demais informações do Candidato na rotina de Funcionários (SRA), na rotina de Admissão o candidato mudará para "admitido" conforme a legenda:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8455146988439/mceclip1.png)  
  
Já o arquivo **RSDEPA2.TXT** é utilizado quando se faz uso da rotina de Seleção Interna rotina (RSPM002), ela irá buscar os dados do cadastro de funcionários para o cadastro de currículos, processo inverso.  
  
Em anexo à este artigo, estão como exemplo os arquivos **RSPDEPA.TXT e RSDEPA2.TXT** padrão do produto.  
  
**Saiba Mais**  
[Artigos Recrutamento e Seleção de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960907-RH-Recrutamento-e-Sele%C3%A7%C3%A3o-de-Pessoal)
