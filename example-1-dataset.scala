// Stanford TMT Example 1 - Loading data
// http://nlp.stanford.edu/software/tmt/0.4/

// tells Scala where to find the TMT classes
import scalanlp.io._;
import scalanlp.stage._;
import scalanlp.stage.text._;
import scalanlp.text.tokenize._;
import scalanlp.pipes.Pipes.global._;

import edu.stanford.nlp.tmt.stage._;
import edu.stanford.nlp.tmt.model.lda._;
import edu.stanford.nlp.tmt.model.llda._;

val source = CSVFile("chinese_ti_and_ab.csv") ~> IDColumn(1);

val tokenizer = {
  WhitespaceTokenizer() ~>            	 // tokenize on space and punctuation
  CaseFolder() ~>                        // lowercase everything
  WordsAndNumbersOnlyFilter() ~>         // ignore non-words and non-numbers
  MinimumLengthFilter(2)				 // take terms with >=3 characters
}

val text = {
  source ~>                              // read from the source file
  Columns(3,4) ~>                        // select column containing text
  Join(" ") ~>							 // join " " between column 3 and 4
  TokenizeWith(tokenizer) ~>             // tokenize with tokenizer above
  TermCounter() ~>                       // collect counts (needed below)
  TermMinimumDocumentCountFilter(4) ~>   // filter terms in <4 docs
  TermDynamicStopListFilter(30) ~>       // filter out 30 most common terms
  DocumentMinimumLengthFilter(5)         // take only docs with >=5 terms
}

val dataset = LDADataset(text);
val params = LDAModelParams(numTopics = 12,dataset = dataset,topicSmoothing = 0.01,termSmoothing = 0.01);
val modelPath = file("F:\\Files\\StanfordTMT\\HE");
TrainCVB0LDA(params, dataset, output=modelPath, maxIterations=1000);

