---
article_id: 360025640474
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 29f2f492a4da1a5d669bfefc850fd883f228d4131d1652834d4bf684b447e07d
fetched_at: '2026-06-28T22:40:47.626140+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus  - SIGACTB - ECF : Y520 COMO GERAR'
type: support-article
updated_at: '2024-07-23T18:24:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025640474-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Y520-COMO-GERAR
---

**Dúvida**Como gerar o Bloco Y520 ?  
  
**Ambiente**Microsiga Protheus  – Contabilidade  – A partir da versão 11.80  
  
**Solução**

Registro Y520: Pagamentos/Recebimentos do Exterior ou de Não Residentes  
  
Manual da Receita demonstra exemplo que como deve ser gerado o registro Y520  
  
<http://sped.rfb.gov.br/arquivo/show/2422>  
  
Exemplo de Preenchimento:  
  
|Y520|R|1|1|10500|100000,00|  
|Y520|: Identificação do tipo do registro.  
|R|: Rendimentos recebidos do exterior.  
|1|: País (1 = Canadá).  
|1|: Forma de recebimento (1 = Operação de Câmbio).  
|10500|: Natureza da operação (10500 = Câmbio Simplificado Simultâneo  
|100000,00: Valor recebido (R$ 100.000,00).

**1)****Conforme as documentações [Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=192094180#Blocos/Registros-blocoy)  ,**o Y520 é informado diretamente dentro do TAF.

Veja os [Registros dos blocos X e Y gerados automaticamente pelo extrator](https://tdn.totvs.com/pages/releaseview.action?pageId=192094180#Blocos/Registros-blocoy)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080906294)

[Blocos/Registros](https://tdn.totvs.com/pages/viewpage.action?pageId=192094180#Blocos/Registros-blocoy)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082001733)

**2)****Acessar a centralizadora de ECF do TAF**

Conforme documentação abaixo ao exportar os dados para o TAF  as perguntas abaixo refletem na geração do bloco Y520   
<http://tdn.totvs.com/display/PROT/ECF0003_Help_wizard_rotina_central_escrituracao_ECF>

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040698953)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039873914)

**3)****Clicar no [Bloco Y](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#ECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoY-Informa%C3%A7%C3%B5esGerais) – Informações Gerais**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080906694)

4) Procurar por Registro Y520 – Pagamentos/Recebimentos do Exterior ou de Não Residentes

### **Bloco Y - Informações Gerais**

**Registro Y001 - Abertura do Bloco Y**  
**Registro Y520 - Pagamentos/Recebimentos do Exterior ou de Não Residentes**

* Tabelas - CFQ (Pag/Rend. Rec. Ext./Não Resid.) / C08 (Países Bco Central/SISCOMEX) / CHK (Natureza da Operação ECF)
* Registro do Layout TOTVS - T104
* Rotina - TAFA329 (Pagamentos ou Rend. Recebidos Exterior/Não Residente)

Existem 2 possibilidades para popular a tabela e gerar o Y520 no TAF, são elas:  
1) Via Integração por [Layout TOTVS T104](https://tdn.totvs.com/pages/releaseview.action?pageId=498722271)  (recomendado para outras marcas, além do Protheus); 

[Veja: Como importar arquivos XML no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027012291-RH-Linha-Protheus-TAF-eSocial-Integra%C3%A7%C3%A3o-Como-importar-arquivos-XML-no-TAF?source=search)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082002093)

2) Por inclusão de cadastro direto no SIGATAF, conforme caminho:  
SIGATAF \ Atualizações \ Movimentos Contábeis \ Bloco Y – Informações Gerais \ Reg.y520-pgto/rec Ext. N. resid ([TAFA329.PRW](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoY-Informa%C3%A7%C3%B5esGerais))  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080907934)

O importante é possuir as tabelas do TAF preenchidas, são elas:

* è CFQ (tabela de negócio, referente aos pagamentos e recebimentos, com essa movimentação, o TAF irá gerar o arquivo de extração com o leiaute Y520);
* è C08 (autocontidas com relação dos países bco central \ Siscomex );
* è CHK (autocontidas com a natureza de operação do ECF);

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082002293)

Geração do arquivo final com o registro Y520  
1) Complemento Cadastral (TAFA050) \ Aba Obrigações Fiscais \ Inserir opção 000005 (ECF)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080908034)

2) Acessar Miscelânea \ Obrigações Fiscais \ Central de Obrigações  
Avançar \ selecionar esfera federal \ Avançar

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080908074)

3) Marcar opção ECF \ Avançar \ Avançar

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082002433)

Criar um identificador de período válido, de acordo com a data de movimentação do Y-520; selecionar versão 0005, um diretório e nome de arquivo válido. Avançar;

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082002473)

Escrituração, selecionar a opção N-ECF original. Finalizar

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082002493)

Selecionar os responsáveis

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080908234)

Marcar todos os blocos, inclusive o Y;

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080908254)

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082002553)

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080908274)

Saiba mais:

[MP - SIGACTB - ECF - Como realizar a geração dos blocos X e Y?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006827952-MP-SIGACTB-ECF-Como-realizar-a-gera%C3%A7%C3%A3o-dos-blocos-X-e-Y-?source=search)  
[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)

[MP - SIGACTB - ECF : Y520 CFQ\_CODNAT / NAT\_OPER NÃO ESTA SENDO GERADO NO ARQUIVO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053359714-MP-SIGACTB-ECF-Y520-CFQ-CODNAT-NAT-OPER-N%C3%83O-ESTA-SENDO-GERADO-NO-ARQUIVO?source=search)
