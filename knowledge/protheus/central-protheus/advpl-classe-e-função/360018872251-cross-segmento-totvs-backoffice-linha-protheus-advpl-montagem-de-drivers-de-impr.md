---
article_id: 360018872251
category: ADVPL - Classe e Função
content_hash: b39f2f30ac7a5d80f92a6919d63b28872c2a4a3953a3a5006e0e3fea8a0c5688
fetched_at: '2026-06-28T22:40:17.006906+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Montagem de Drivers
  de Impressão
type: support-article
updated_at: '2023-03-17T17:49:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018872251-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Montagem-de-Drivers-de-Impress%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Utilizo a classe **setprint** e preciso alterar o tamanho do fonte. Preciso de um tutorial de configuração dos arquivos de configuração de driver (.DRV) que ficam na pasta SYSTEM?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução****Considerações gerais**Um arquivo de driver deve ser editado num editor de texto simples e obedece o seguinte padrão:  
  
HP 660 C A4     Þ Descrição do driver e para qual tipo de papel foi desenvolvido  
[080C] ...          Þ Linha para impressão em 80 colunas no formato comprimido  
[080E] ...          Þ Linha para impressão em 80 colunas no formato expandido  
[132C] ...  
[132E] ...  
....  
  
Normalmente os comandos da linguagem PCL tem a seguinte estrutura:  
**<****Escape****>****&l#@**, sendo:  
<Escape>    Sequência de caracteres enviada a impressora, representada pela função chr(27)  
&l                Categoria dos comandos. Deve ser digitado exatamente desta forma, o símbolo & junto a letra l minúscula.  
#                 Campo de valor. Contém caracteres alfabéticos e numéricos.  
@                Término da sequência escape. Normalmente uma letra maiúscula.  
  
< Tipo de Relatório > < Orientação > + < Tamanho do Papel > + < Linhas por Polegada > +  <Sequência padrão >+ < Conjunto do Símbolos  > + < Seleção de Fonte >  
Cada uma das partes que compõe a linha devem ser separadas pelo sinal “+”, exceto quando não for mencionado o mesmo na nomenclatura.  
  
**Estrutura de cada linha****Tipo de Relatório**[NNNX]  Onde: NNN = Número de colunas do relatório  080, 132 ou 220

X       = C – Comprimido           E – Expandido  
(\*) O uso dos colchetes é obrigatório  
 **Orientação** Esta seqüência define a orientação do papel.  
 Chr(27)+”&l#O”, onde # = 0 – vertical  
                                      1 – horizontal  
                                      2 – vertical invertido  
                                      3 – horizontal invertido

**Margens na Impressora**1 – Margem esquerda = Chr(27)+”&a#L”  , onde # No. de linhas / colunas  
2 – Margem direita       = Chr(27)+”&a#M”  
3 – Margem Superior   = Chr(27)+&l#E  
  
**Tamanho do Papel**Chr(27)+”&l#A”, onde # =  1 – Executivo  
                                          2 – Carta  
                                          3 – Legal  
                                         25 – A5  
                                         26 – A4

**Linhas por polegada**Chr(27)+”&l#D”, onde # = 1, 2, 3 , 4 , 5, 6, 12, 16, 24 ou 48  
  
**Sequência****Padrão**Esta seqüência deve ser inserida em todas as linhas.  
Chr(27)+"&l72P"  
  
**Conjunto de Símbolos**Define o conjunto de caracteres a ser utilizado na impressora.  
Chr(27)+”(#”, onde # =     8U     HP Roman 6  
                                       10U    IBM PC Americando (PC-8) Codepage 437  
                                       12U    IBM PC Europeu Codepage 850  
                                         8M     Matemático  
                                        19U    Windows 3.1 Latin 1

**Seleção de Fonte**A seleção da fonte é uma extensa cadeia de caracteres com o seguinte padrão:  
chr(27)+"(s**A**p**B**h**C**v**D**s**E**b3T", onde:

A – Tipo de espaçamento, sendo    0 = fixo  
                                                        1 = proporcional

B – Número de caracteres por polegada  
C – Altura da fonte em pontos  
D – Estilo da fonte, sendo   0 = normal  
                                            1 = itálico  
                                            4 = condensado  
                                            5 = itálico condensado

E – Espessura do traço, sendo    0 = médio  
                                                   1 = seminegrito  
                                                   3 = negrito  
                                                   4 = extranegrito

Exemplo de uma seqüência para seleção de fontes: **chr(27)+"(s0p20h6v0s0b3T"**Exemplo de uma linha completa:

```
[080C]CHR(27)+"&l0O"+chr(27)+"&l2A"+chr(27)+"&l07D"+chr(27)+"&l72P”+chr(27)+"(12U"+chr(27)+"(s0p20h6v0s0b3T"
```

**Saiba mais**[Driver de Impressão não especificado](http://tdn.totvs.com/pages/releaseview.action?pageId=108662115)  
[NODRIVER - MV\_DRIVER - Driver de Impressão não especificado.](http://tdn.totvs.com/pages/viewpage.action?pageId=268570634)
